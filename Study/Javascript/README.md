### 출력

```javascript
// 한 줄 출력
console.log("hello, world");

// 여러 줄 출력
for (let i = 1; i <= 100; i++) {
  answer += i + "\n";
}

// 반올림
let x = 123.456;
console.log(x.toFixed(2));
```

### 입력

```javascript
// 입력 데이터가 텍스트 파일 형태인 경우
// 파일 시스템 모듈을 사용
// fs를 우선적으로 쓰고, fs가 되지 않는 상황에서는 readline 사용

// fs 모듈
// 여러줄 입력 받기
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// readline 모듈
// 여러줄 입력 받기
const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  // 콘솔 입력 창에서 enter를 입력할 때 마다 호출
  input.push(line);
}).on("close", function () {
  // ctrl + c 혹은 ctrl + d 입력하면 호출
  console.log(input);
  process.exit();
});

// 한 줄 내용 나누기
let [a, b] = input[0].split(" ").map(Number);
```

### 자료형 변환

```javascript
// 수 -> 문자열
a = 777;
String(a);

// 문자열 -> 수
a = "777";
Number(a);
```

### 함수

```javascript
// reduce()
// 배열의 모든 원소에 대해 특정한 연산을 순차적으로 적용.
// 배열의 각 요소에 reducer 함수를 실행한 뒤에 하나의 결과 반환.
// reduce((accumulator, currentValue) => (반환값))

let minValue = data.reduce((a, b) => Math.min(a, b));
let summary = data.reduce((a, b) => a + b);
```

### Array

```javascript
// 배열 초기화
let arr = new Array(5).fill(0);
```

### Set

```javascript
let mySet = new Set();

// 삽입
mySet.add(3);

// 원소의 개수
mySet.size;

// 포함 여부
mySet.has(3);

// 제거
mySet.delect(3);

// 원소 하나씩 출력
for (let item of mySet) console.log(item);
```

### 수학

```javascript
// 몫
prseInt(a / b);

// 큰 값
Math.max(a, b, c);
Math.max(...arr);

// 작은 값
Math.min(a, b, c);
Math.min(...arr);
```

### use strict

```javascript
// 기존에 무시되던 에러들을 잡고, 엔진의 최적화 작업을 어렵게 만드는 것들을 잡아준다.
"use strict";
```
