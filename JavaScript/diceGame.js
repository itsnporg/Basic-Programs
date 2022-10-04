
var firstNum = Math.floor(Math.random()*6+1);

var secondNum = Math.floor(Math.random()*6+1);

    console.log(`
    player1  =>${firstNum}
    player2  =>${secondNum}`);
 
     
    if(firstNum>secondNum) console.log("player1 won! ");
    else if(secondNum>firstNum) console.log("player2 won!");
    else if(firstNum==secondNum) console.log("Draw play again!");

