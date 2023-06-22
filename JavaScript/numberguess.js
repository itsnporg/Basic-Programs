let a = 1;
let b = 10;
let secret_number = Math.round(a+(b-a)*Math.random());
function game(){
    let guess = 1;
    while(guess <= 3){
        guessed_number = parseInt(prompt("Enter your guess"))
        if(guessed_number == secret_number){
            alert("You have guessd the number!!");
            break
        }
        else{
            prompt("Try again")
        }
        guess++;
    }
    if(guess == 3){
        alert("You have failed")
    }
}
game();