const display = document.querySelector("input"),
  button = document.querySelector("button");
let chars =
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]:;?><,./-=";

const generate = () => {
  let i,
    randomPassword = "";
  for (i = 0; i < 16; i++) {
    randomPassword =
      randomPassword + chars.charAt(Math.floor(Math.random() * chars.length));
  }
  display.value = randomPassword;
};

generate();

button.onclick = () => generate();

display.addEventListener("click", () => copy());

function copy() {
  display.select();
  document.execCommand("copy");
}
