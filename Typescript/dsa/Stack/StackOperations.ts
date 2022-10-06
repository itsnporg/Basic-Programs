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
    top: number;
    constructor() {
        this.items = [];
        this.top = -1;
    }
    push = push;
    pop = pop;
    peek = peek;
    isEmpty = isEmpty;
    printStack = printStack;
}

function push(data: any) {
    this.items.push(data);
    this.top++;
}
//pop operation on stack
function pop() {
    if (this.top === -1) {
        return "Stack is empty";
    }
    this.top--;
    return this.items.pop();
}
//peek operation on stack
function peek() {
    return this.items[this.top];
}
// Check if the stack is empty
function isEmpty() {
    return this.top === -1;
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
console.log(stack.printStack());
//peek operation
console.log(stack.peek());
//pop operation
console.log(stack.pop());
//printing stack elements
console.log(stack.printStack());
//isEmpty operation
console.log(stack.isEmpty());

