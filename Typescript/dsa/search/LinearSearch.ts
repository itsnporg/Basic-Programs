// search for index of a number in a array of numbers
// Complexity: O(N)

interface Array<T> {
  linearSearch(required_number: number): number | void;
}

Array.prototype.linearSearch = function(
  required_number: number
): number | undefined {
  for (let i = 0; i < this.length; i++) {
    if (this[i] === required_number) {
      return i;
    }
  }
};

const arr: Array<number> = [];

for (let i = 1; i <= 1000000; i++) {
  arr.push(i);
}

const startTime = Date.now();
const index = arr.linearSearch(999999);
const endTime = Date.now();

console.log(`Required index: ${index}.`);
console.log(`Time taken: ${endTime - startTime}.`);
