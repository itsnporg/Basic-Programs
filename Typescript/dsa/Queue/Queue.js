var Queue = /** @class */ (function () {
    function Queue(size) {
        this.items = [];
        this.front = 0;
        this.rear = 0;
        this.size = 0;
        this.enqueue = enqueue;
        this.dequeue = dequeue;
        this.isQueueEmpty = isQueueEmpty;
        this.peek = peek;
        this.printQueue = printQueue;
        //size of the queue
        this.size = size;
    }
    return Queue;
}());
//pushing an element in queue
function enqueue(data) {
    if (this.rear === this.size) {
        console.log("Queue is full");
        return;
    }
    this.items[this.rear] = data;
    this.rear++;
}
//poping and elememnt from queue
function dequeue() {
    if (this.front === this.rear) {
        console.log("Queue is empty");
        return;
    }
    var data = this.items[this.front];
    this.front++;
    return data;
}
function peek() {
    return this.items[this.front];
}
function isQueueEmpty() {
    return this.front === this.rear;
}
function printQueue() {
    if (this.isQueueEmpty()) {
        console.log("Queue is empty");
        return;
    }
    var str = "";
    for (var i = this.front; i < this.rear; i++) {
        str += this.items[i] + " ";
    }
    return str;
}
//creating an object of Queue class with size Queue size 5
var queue = new Queue(5);
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.enqueue(50);
//queue.enqueue(60); //Queue is full
console.log(queue.printQueue());
//dequeueing an element from queue
console.log(queue.dequeue());
//printing an elemets from queue
console.log(queue.printQueue());
//peeking an element from queue
console.log(queue.peek());
//checking if the  queue is empty or not
console.log(queue.isQueueEmpty());
