class Queue {
  constructor() {
    this.items = {};
    this.headIndex = 0;
    this.tailIndex = 0;
  }
  enqueue(item) {
    this.items[this.tailIndex] = item;
    this.tailIndex++;
  }
  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }
    const item = this.items[this.headIndex];
    delete this.items[this.headIndex];
    this.headIndex++;

    if (this.isEmpty()) {
      this.headIndex = 0;
      this.tailIndex = 0;
      this.items = {};
    }
    return item;
  }
  peek() {
    return this.items[this.headIndex];
  }
  getSize() {
    return this.tailIndex - this.headIndex;
  }
  isEmpty() {
    // return Object.keys(this.items).length == 0;
    return this.tailIndex == this.headIndex;
  }
  print() {
    console.log(Object.values(this.items));
  }
}

const q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.print();
q.dequeue();
q.dequeue();
q.print();
console.log(q.isEmpty());
