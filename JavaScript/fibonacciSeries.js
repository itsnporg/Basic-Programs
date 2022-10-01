/* 
In fibonacci series, next number is the sum of previous two numbers. 
for example 0, 1, 1, 2, 3, 5, 8, 13 etc. 
The first two numbers of fibonacci series are 0 and 1
*/

// take user input
const numOfTerms = Number(prompt("Enter the number of terms: "));

let firstNum = 0;
let secondNum = 1;
let nextTerm;
let result = "";

console.log(`Fibonacci Series up to ${numOfTerms} terms: `);

// iterate upto number of times user has given input
for (let i = 1; i <= numOfTerms; i++) {
	// add comma after each output number until it's not the last one
	if (numOfTerms === i) {
		result += firstNum.toString();
	} else {
		result += firstNum.toString() + ",";
	}

	// update values for next iteration
	nextTerm = firstNum + secondNum;
	firstNum = secondNum;
	secondNum = nextTerm;
}

console.log(result);

// example: for numOfTerms=5, expected output is: "0,1,1,2,3"
