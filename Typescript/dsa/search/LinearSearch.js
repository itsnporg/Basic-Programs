// search for index of a number in a array of numbers
// Complexity: O(N)
Array.prototype.linearSearch = function(required_number) {
  for (var i = 0; i < this.length; i++) {
    if (this[i] === required_number) {
      return i;
    }
  }
};
var arr = [];
for (var i = 1; i <= 1000000; i++) {
  arr.push(i);
}
var startTime = Date.now();
var index = arr.linearSearch(999999);
var endTime = Date.now();
console.log("Required index: ".concat(index, "."));
console.log("Time taken: ".concat(endTime - startTime, "."));
