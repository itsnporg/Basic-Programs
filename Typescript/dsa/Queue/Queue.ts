interface Queue {
    items: any[];
    size: number;
    front: number;
    rear: number;
    enqueue(data: any): void;
    dequeue(): any;
    peek(): any;
    isQueueEmpty(): boolean;
    printQueue(): string | undefined;
}

class Queue {
     items: any[] = [];
     front: number = 0;
     rear: number = 0;
     size: number = 0;
     //initialize the queue
    constructor(size: number) {
        //size of the queue
        this.size = size; 
    }
    public enqueue = enqueue;
    public dequeue = dequeue;
    public isQueueEmpty = isQueueEmpty;
    public peek = peek;
    public printQueue = printQueue;
} 

//pushing an element in queue
function enqueue(data: any) {
    if (this.rear === this.size) {
        console.log("Queue is full");
        return; //if the queue is full then we can't add any element in it
    }
    this.items[this.rear] = data; //adding the element in the queue
    this.rear++; //incrementing the rear pointer to point to the next element in the queue
}
//poping and elememnt from queue
function dequeue() {
    if (this.front === this.rear) {
        console.log("Queue is empty");
        return; //if the queue is empty then we can't remove any element from it
    }
    let data = this.items[this.front]; //storing the first element of the queue in data variable
    this.front++; //incrementing the front pointer to point to the next element in the queue
    return data; //returning the first element of the queue which is removed
}
function peek() {
    return this.items[this.front]; //returning the first element of the queue
}
function isQueueEmpty() {
    return this.front === this.rear; //if the front and rear pointer are equal then the queue is empty
}
function printQueue() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return; //if the queue is empty then we can't print any elements from it
    } 
    let str = "";
    for (let i = this.front; i < this.rear; i++) {
        str += this.items[i] + " ";
    }
    return str;
}

//creating an object of Queue class with size Queue size 5
const queue = new Queue(5);
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.enqueue(50);
//queue.enqueue(60); //Queue is full

console.log(queue.printQueue()); //10 20 30 40 50

//dequeueing an element from queue
console.log(queue.dequeue()); //10 will be removed
//printing an elemets from queue
console.log(queue.printQueue()); //20 30 40 50 
//peeking an element from queue
console.log(queue.peek()); //20
//checking if the  queue is empty or not
console.log(queue.isQueueEmpty()); // it returns  false

