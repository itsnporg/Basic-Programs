interface circularQueue {
    items: any[];
    size: number;
    frontofQueue: number;
    rearofQueue: number;
    enqueueQueue(data: any): void;
    dequeue(): any;
    peek(): any;
    isQueueEmpty(): boolean;
    isQueueFull(): boolean;
    printQueue(): string | undefined;
}

class circularQueue {
    arr: number[];
    frontofQueue: number;
    rearofQueue: number;
    size: number;
    capacity: number;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.arr = new Array(capacity);
        this.frontofQueue = 0;
        this.rearofQueue = 0;
        this.size = 0;
    }
    public enqueueQueue = enqueueQueue;
    public dequeueQueue = dequeueQueue;
    public peekFront = peekFront;
    public peekRear = peekRear;
    public isQueueEmpty = isQueueEmpty;
    public isQueueFull = isQueueFull;
    public printQueue = printQueue;


}

//pushing an element in circular queue

function enqueueQueue(data: any) {
    if (this.isQueueFull()) {
        console.log("Queue is full");
        return;
    }
    this.arr[this.rearofQueue] = data;
    this.rearofQueue = (this.rearofQueue + 1);
    this.size++;
}

//removing an element from circular queue
function dequeueQueue() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return;
    }
    let data = this.arr[this.frontofQueue];
    this.frontofQueue = (this.frontofQueue + 1);
    this.size--;
    return data;
}

//peeking an element from front of circular queue
function peekFront() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return;
    }
    return this.arr[this.frontofQueue];
}

//peeking an element from rear of circular queue
function peekRear() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return;
    }
    return this.arr[this.rearofQueue - 1];
}

//checking if circular queue is empty or not

function isQueueEmpty() {
    return this.size === 0;
}
//check if circular queue is full or not
function isQueueFull() {
    return this.size === this.capacity;
}

//printing the all elements of circular queue
function printQueue() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return;
    }
    let str = "";
    for (let i = this.frontofQueue; i < this.rearofQueue; i++) {
        str += this.arr[i] + " ";
    }
    return str;
}

var circularqueue = new circularQueue(5);

//pushing elements in circular queue
circularqueue.enqueueQueue(1);
circularqueue.enqueueQueue(2);
circularqueue.enqueueQueue(3);
circularqueue.enqueueQueue(4);
circularqueue.enqueueQueue(5);

//printing the elements of circular queue
console.log(circularqueue.printQueue()); //1 2 3 4 5
//removing an element from circular queue
console.log(circularqueue.dequeueQueue()); //1
//peeking an element from front of circular queue
console.log(circularqueue.peekFront()); //2
//peeking an element from rear of circular queue
console.log(circularqueue.peekRear()); //5
//printing the elements of circular queue
console.log(circularqueue.printQueue()); //2 3 4 5
//checking if circular queue is empty or not
console.log(circularqueue.isQueueEmpty()); //false
