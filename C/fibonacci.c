/*
In fibonacci series, next number is the sum of previous two numbers.
for example 0, 1, 1, 2, 3, 5, 8, 13 etc.
The first two numbers of fibonacci series are 0 and 1
*/

#include <stdio.h>

// recursive function for printing the fibonacci.
int fibonacci(int number1, int number2, int numOfTerms) {
  static int count = 0;

  if (count >= numOfTerms) {
    return 0;
  }

  printf("%d\n", number1 + number2);
  count++;
  return fibonacci(number2, number1 + number2, numOfTerms);
}

int main() {
  int firstTerm = 0;
  int secondTerm = 1;
  int numOfTerms = 0;

  printf("Enter the number of terms you want to print: ");
  scanf("%d", &numOfTerms);

  printf("%d\n%d\n", firstTerm, secondTerm);

  fibonacci(firstTerm, secondTerm, numOfTerms - 2);
  return 0;
}