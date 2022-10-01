interface Array<T> {
  bubbleSort: () => void;
}

Array.prototype.bubbleSort = function() {
  let tempNumber: number;
  for (let i = 0; i < this.length; i++) {
    for (let j = 0; j < this.length; j++) {
      // if j indexed number is greater than i indexed number interchange the positions
      if (this[j] > this[i]) {
        tempNumber = this[j];
        this[j] = this[i];
        this[i] = tempNumber;
      }
    }
  }
};

const arr = [2, 1, 3, 2, 4, 10, 0, -1, 200, -300];
arr.bubbleSort();
console.log(arr);
