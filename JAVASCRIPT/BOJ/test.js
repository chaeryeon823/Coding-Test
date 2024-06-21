let fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');
let time = input[0].split(' ');
let hour = Number(time[0]);
let min = Number(time[1]);
let oven = Number(input[1]);

min += oven;
if (min >= 60) {
  hour += parseInt(min / 60);
  min = min % 60;
}
if (hour > 23) {
  hour -= 23;
}

console.log(hour, min);
