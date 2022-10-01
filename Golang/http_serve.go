package main

import (
    "fmt"
    "io"
    "log"
    "net/http"
)

func handlerGreeting(w http.ResponseWriter, r * http.Request) {
    log.Printf("Endpoint Hit")
    io.WriteString(w, "Hello World")
}

func main() {
    fmt.Println("HTTP Served")
    http.HandleFunc("/", handlerGreeting)

    err: = http.ListenAndServe(":8000", nil)
    if err != nil {
        panic(err)
    }
}