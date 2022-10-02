let userName = prompt('Please enter your name', '');
let userChoice = prompt('Please enter your choice, "DC" or "Marvel":', '');
let randomNumber = Math.floor(Math.random() * 8);
let superhero = '';
let universe=userChoice.toLowerCase();

userName ? console.log(`Hello, ${userName}`) : console.log('Hello!');
if(universe == 'dc'){
    switch(randomNumber) {
        case 0:
            superhero = 'Batman\n';
          break;
        case 1:
            superhero = 'Green Arrow\n';
          break;  
        case 2:
            superhero = 'Aquaman\n';
          break;  
        case 3:
            superhero = 'Deathstroke\n';
          break;  
        case 4:
            superhero = 'Cat Woman\n';
          break;  
        case 5:
            superhero = 'Superman\n';
          break;  
        case 6:
            superhero = 'Black Adam\n';
          break; 
        case 7:
            superhero = 'Doctor Fate\n';
          break;  
      }
}

if(universe == 'marvel'){
    switch(randomNumber) {
        case 0:
            superhero = 'Iron Man\n';
          break;
        case 1:
            superhero = 'Doctor Strange\n';
          break;  
        case 2:
            superhero = 'Hawkeye\n';
          break;  
        case 3:
            superhero = 'Black Widow\n';
          break;  
        case 4:
            superhero = 'Thor\n';
          break;  
        case 5:
            superhero = 'Doctor Strange\n';
          break;  
        case 6:
            superhero = 'Groot\n';
          break; 
        case 7:
            superhero = 'Star Lord\n';
          break;  
      }
}
console.log(`${userName}'s question: `);
console.log(`Hey, ${userName}! If you were in the ${userChoice}.. You wold have been ${superhero}!!`);