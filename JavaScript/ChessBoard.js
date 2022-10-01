var bindingSize = 8;
var printString = "";
var isSpace = false;

for (let i = 1; i <= bindingSize; i++) {
  i % 2 == 0 ? (isSpace = true) : (isSpace = false);
  for (let k = 0; k < bindingSize; k++) {
    if (isSpace) {
      printString = printString + "#";
      isSpace = false;
    } else {
      printString = printString + " ";
      isSpace = true;
    }
  }
  printString = printString + "\n";
}
console.log(printString);
