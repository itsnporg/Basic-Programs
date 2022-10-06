interface Stack {
    items: any[];
    top: number;
    push: (data: any) => void;
    pop: () => any;
    peek: () => any;
    isEmpty: () => boolean;
    printStack: () => string;
}

//push operation on stack
class Stack {
    items: any[];
    top: number; //top pointer
    constructor() {
        this.items = []; //initialize the stack
        this.top = -1; //initialize the top pointer
    }
    push = push;
    pop = pop;
    peek = peek;
    isEmpty = isEmpty;
    printStack = printStack;
}

function push(data: any) {
    this.items.push(data); //adding the element in the top of  stack
    this.top++;
}
//pop operation on stack
function pop() {
    if (this.top === -1) {
        return "Stack is empty"; //if the stack is empty then we can't remove any element from it
    }
    this.top--;
    return this.items.pop();
}
//peek operation on stack
function peek() {
    return this.items[this.top]; //returning the top element of the stack
}
// Check if the stack is empty
function isEmpty() {
    return this.top === -1; //if the top is -1 then the stack is empty
}
//print the Stack operation on stack
function printStack() {
    let str = "";
    for (let i = 0; i <= this.top; i++) {
        str += this.items[i] + " ";
    }
    return str;
}

//creating object of Stack class
const stack = new Stack();
//pushing elements in stack
stack.push(10);
stack.push(20);
stack.push(30);
stack.push(40);
stack.push(50);
//printing stack elements
console.log(stack.printStack()); //output: 10 20 30 40 50 (top to bottom)
//peek operation
console.log(stack.peek()); //output: 50 (top element of the stack)
//pop operation
console.log(stack.pop()); //output: 50 (removed top element of the stack)
//printing stack elements
console.log(stack.printStack()); //output: 10 20 30 40 (after removing top element of the stack)
//isEmpty operation
console.log(stack.isEmpty()); //output: false (stack is not empty)

