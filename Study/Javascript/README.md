### 출력

```javascript
// 한 줄 출력
console.log("hello, world");

// 여러 줄 출력
for (let i = 1; i <= 100; i++) {
    answer += i + "\n";
}

// 변수랑 문자열 섞어서 출력
console.log(`${a} + ${b} = ${a + b}`);

// 배열 원소 하나씩 출력
for (let item of arr) console.log(item);

// 객체 원소 하나씩 출력
for (let key in obj) console.log(key, obj[key]);
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

// 입력 받은 내용 전부 정수로 변환
data = input.map((x) => Number(x));
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

### 객체

> key-value

```javascript
// 객체 생성
const obj = new Object();
const obj = {};
const obj = {
    name: "chaeryeon",
    familyName: "Kang",
    age: "1000",
};

// 객체 추가
obj["phone"] = "012345678";

// 객체 삭제
delete obj["phone"];

// key 존재 여부
"email" in obj;

// key 배열
Object.keys(obj);

// value 배열
Object.values(obj);
```

### 배열

> 연속적인 형태로 구성된 구조  
> 자바스크립트는 동적 배열

```javascript
// 배열 생성
let arr = [];
let arr = new Array();

// 배열 초기화
let arr = new Array(5).fill(0);
let arr = Array.from({ length: 5 }, () => 7);
let arr = Array.from(Array(5), () => 7);
let arr = Array.from(Array(5), (_, k) => k);

// 배열 요소 삽입
arr.push(1);
arr.splice(3, 0, 128); // O(N)

// 배열 요소 제거
arr.splice(3, 1); // O(N)
arr.pop();

// 배열의 첫 요소 뽑기 ( deque, leftpop)
arr.shift();

// 배열의 첫 요소 추가 ( deque, leftpush)
arr.unshift(10);

// from
Array.from("foo"); //['f','o','o']
Array.from([1, 2, 3], (x) => x + x); //[2,4,6]

// 2치원 배열
let arr = Array.from(Array(4), () => new Array(5));

let arr = new Array(3);
for (let i = 0; i < arr.length; i++) {
    arr[i] = Array.from({ length: 4 }, (_, j) => i * 4 + j);
}

// 배열 합치기
arr1.concat(arr2); //O(N)

// 배열 슬라이싱
arr.slice(1, 4); //O(N)

// 배열의 값으로 인덱스 찾기
arr.indexOf(3); //O(N)

// 배열 거꾸로 전환
arr.reverse(); // 원본 변형
arr.slice().reverse(); // 원본 변형 없음.
```

### Set

```javascript
let mySet = new Set();

// set으로 중복 제거 하고 array로
uniqueArr1 = Array.from(new Set(arr));
uniqueArr2 = [...new Set(arr)];

// 삽입
mySet.add(3);

// 원소의 개수
mySet.size;

// 포함 여부
mySet.has(3);

// 제거
mySet.delect(3);
```

### 수학

```javascript
// 몫
prseInt(a / b);

// 큰 값
Math.max(a, b, c);
Math.max(...arr);
arr.reduce((a, b) => Math.max(a, b)); //제일 빠르긴함.

// 작은 값
Math.min(a, b, c);
Math.min(...arr);
arr.reduce((a, b) => Math.min(a, b));

// 반올림
let x = 123.456;
console.log(x.toFixed(2));
```

### 문자열

```javascript
// 인덱스로 문자열에서 문자 얻기
s.charAt(index); // 범위가 넘으면 ''
s[index]; // 범위가 넘으면 undefined

// 문자 반복하기
c.repeat(times);

// 문자열 양끝 공백 제거
s.trim();

// 배열 문자열로 합치기
arr.join("");

// 문자열 자르기
s.substring(0, 2);
s.substring(2);
```

### 스택

> FILO  
> 자바스크립트에서 stack은 배열 자료형을 사용.  
> push O(1)  
> pop O(1)  
> top O(1)  
> empty O(1)

### 큐

> FIFO  
> 삽입 O(1)
> 삭제 O(1)

```javascript
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

        // 너무 커지는 것을 방지
        // if (this.isEmpty()) {
        //   this.headIndex = 0;
        //   this.tailIndex = 0;
        //   this.items = {};
        // }
        return item;
    }
    peek() {
        return this.items[this.headIndex];
    }
    getSize() {
        return this.tailIndex - this.headIndex;
    }
    isEmpty() {
        return this.tailIndex == this.headIndex;
    }
    print() {
        console.log(Object.values(this.items));
    }
}
```

```javascript
class Queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }

    enqueue(value) {
        this.queue[this.rear++] = value;
    }

    dequeue() {
        const value = this.queue[this.front];
        delete this.queue[this.front];
        this.front++;
        return value;
    }

    size() {
        return this.rear - this.front;
    }

    peek() {
        return this.queue[this.front];
    }
}
```

### use strict

```javascript
// 기존에 무시되던 에러들을 잡고, 엔진의 최적화 작업을 어렵게 만드는 것들을 잡아준다.
"use strict";
```

## 조각코드

### 1 ~ N 까지의 합

```javascript
// 반복문으로 사용할 수 있지만, 등차수열의 합 공식을 활용하면 빠르게 계산 가능
answer = (N * (N + 1)) / 2;
```
