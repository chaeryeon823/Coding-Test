let fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');
let mySet = new Set(input[0].split(' ').map(Number));
let answer = 0;
if (mySet.size == 1) {
  answer = 10000 + mySet[0] * 1000;
} else if (mySet.size == 2) {
  answer = 1000 + Math.max(...mySet) * 100;
} else {
  answer = Math.max(...mySet) * 100;
}
console.log(answer);
