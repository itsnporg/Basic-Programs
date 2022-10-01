// search for index of a number in a array of numbers
// Note: this alorithm is faster than linear search but array must be sorted
// Complexity: O(logN)
Array.prototype.binarySearch = function(required_number) {
  var low = 0;
  var high = this.length;
  while (low < high) {
    var midIndex = Math.floor(low + (high - low) / 2);
    var midNumber = this[midIndex];
    // found number just return it
    if (midNumber === required_number) {
      return midIndex;
      // the number is less than required_number set low index to midIndex
    } else if (midNumber < required_number) {
      low = midIndex + 1;
    } else {
      // the number is greater than required_number set high index to midIndex
      high = midIndex;
    }
  }
};
var arr = [];
for (var i = 1; i <= 1000000; i++) {
  arr.push(i);
}
var startTime = Date.now();
var index = arr.binarySearch(999999);
var endTime = Date.now();
console.log("Required index: ".concat(index, "."));
console.log("Time taken: ".concat(endTime - startTime, "."));
