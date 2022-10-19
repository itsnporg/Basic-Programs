//if we make a function async, it will return a promise

async function myFunc(){
    console.log("Before await"); //this will run second
    const response = await fetch('https://api.github.com/users');
    const users = await response.json();//it will convert dat into json
    console.log("After awaiting"); //this code will run before the above await code //this will run sixth
    return users;
}

console.log("Before declaring"); //this will run first
let a = myFunc();
console.log("after declaring"); //this will run third

a.then(data => console.log(data)) //this will run last
console.log("after calling a"); //this will run fifth