package main

import (
	"bufio"
	crand "crypto/rand"
	"fmt"
	"log"
	"math/big"
	"os"
	"strings"

	"github.com/ogier/pflag"
)

var (
	wordarray []string
	numarray  []int
	endOfFile int
	makepass  string
)

func makeSecureIntArray(min, max, flag int) {
	for i := 0; i < flag; i++ {
		bi, _ := crand.Int(crand.Reader, big.NewInt(int64(max-min)))
		numarray = append(numarray, min+int(bi.Int64()))
	}
}

// Bubble sort, O(n^2)
func sortIntArray() {
	n := len(numarray)
	swapped := true
	for swapped {
		swapped = false
		for i := 1; i < n; i++ {
			if numarray[i-1] > numarray[i] {
				numarray[i], numarray[i-1] = numarray[i-1], numarray[i]
				swapped = true
			}
		}
	}
}

func getGoDiceWords() string {
	return "./words.txt"
}

func getEOF() int {
	f, err := os.Open(getGoDiceWords())
	if err != nil {
		panic(err)
	}

	rd := bufio.NewReader(f)

	l := 0
	for {
		_, err := rd.ReadString('\n')
		if err != nil {
			break
		}
		l++
	}
	return l
}

func getWord() string {

	f, err := os.Open(getGoDiceWords())
	if err != nil {
		panic(err)
	}

	rd := bufio.NewReader(f)

	l := 0
	v := 0
	t := numarray[v]
	for {
		l++
		line, err := rd.ReadString('\n')
		if err != nil {
			break
		}
		if l == t {
			if v < len(numarray)-1 {
				v++
			}
			t = numarray[v]
			line = strings.TrimSpace(line)
			wordarray = append(wordarray, line)
		}
		if err != nil {
			break
		}
	}
	return ""
}

func main() {
	var lengthRaw = pflag.IntP("length", "l", 6, "Declares number of words in password (default: 6")
	pflag.Parse()
	passwordLength := *lengthRaw
	if passwordLength <= 0 {
		log.Fatal("Index out of range, please supply a number < 0")
	}
	endOfFile = getEOF()
	makeSecureIntArray(0, endOfFile, passwordLength)
	sortIntArray()
	getWord()

	for i := 0; i < len(wordarray); i++ {
		makepass += wordarray[i] + " "
	}

	fmt.Println(makepass)
}
