function countString(string, alphabet) {
  var totalChar = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] == alphabet) {
      totalChar++;
    }
  }
  return totalChar;
}
console.log(countString("Alphabet", "b"));
