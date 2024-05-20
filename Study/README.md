## 0. 코딩테스트 파이썬 필수 문법

### 입력

```python
# 정수
n = int(sys.stdin.readline().rstrip())

# 한줄에 여러 변수
n, m, k = map(int, sys.stdin.redline().split())

# 리스트
data = list(map(int, sys.stdin.redline().split())

# n개의 줄 입력
for i in range(n):
  data.append(int(sys.stdin.readline().rstrip()))

cards = [int(sys.stdin.readline()) for i in range(N)]

# 문자열 리스트
plan = sys.stdin.readline().split()
```

### 문자열

- [문자열 문법 모음](https://github.com/chaeryeon823/Coding-Test/blob/main/Study/StringFunc.md)

### 리스트

```python
# 인덱스로 요소 제거하기
data.pop(index)

# 값으로 제거하기
data.remove(value)


# 리스트 정렬하기
data.sort()
data = sorted(data)
# 정렬할 때 조건은 sorted 함수 안 key 값 활용
data = sorted(data, key = lambda x : x*3, reverse=True)

# 2차원 리스트 정렬하기
data.sort(reverse=True)
data = sorted(data, reverse = True)

# 리스트에서 가장 큰 수 찾기
value = max(data)

# 리스트에서 가장 작은 수 찾기
value = min(data)

# 리스트 크기 구하기
len(data)

# 리스트 내 전체 합
sum(data)

# 리스트 내 가장 큰 수의 인덱스 찾기
data.index(max(data))

# 리스트에서 최대 빈도 원소 구하기(Counter 사용)
from collections import Conter
c = Counter(list)
max_item = count_items.most_common(n=1)
max_item = max(c, key = c.get)

# 리스트 요소만 출력
print(*a)

# 리스트의 모든 요소를 하나의 문자열로 (요소는 문자만 가능)
''.join(data)

# 인덱싱
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
A[::3]
# [1, 4, 7]

```

### 딕셔너리

> - 딕셔너리의 기본은 {Key1: Value1, Key2: Value2, ...} 이다.
> - key는 고유 식별자 이므로 중복될 수 없다. 기존 key에 새 value를 할당하면 이전 값이 대체된다.
> - value에는 list, tuple 등 모든 데이터 유형이 될 수 있다.

```python
# 딕셔너리 쌍 추가
dict[1] = "a"

# 딕셔너리 쌍 삭제
del dic[1]

# 딕셔너리에서 최대 빈도 원소 구하기
max(dict, key=dict.get)

# 딕셔너리에서 key 값만
dict.keys()  # dict_keys 객체로 반환
list(dict.keys())

# 딕셔너리에서 value 값만
dict.values()  # dict_values 객체로 반환
list(dict.values())

# 딕셔너리 key, value 쌍 얻기
dict.items() # key와 value를 튜플로 묶은 dict_itmes객체로 반환

# 딕셔너리 비우기
dict.clear()

# 키가 딕셔너리 않에 존재하는지
1 in dict

# value 값을 기준으로 오름차순 정렬
sorted(dic.items(), key=lambda x:x[1]))       # 딕셔너리를 튜플로 바꿔 오름차순 정렬
dict(sorted(dic.items(), key=lambda x:x[1]))) # 튜플로 바꿔 정렬 후, 다시 딕셔너리로

# key 값을 기준으로 오름차순 정렬
sorted(dic.items())
dict(sorted(dic.items())
```

### 집합

> - set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용됨.
> - 중복을 허용하지 않는다.
> - 순서가 없다.
> - 인덱싱을 통해 요솟값을 얻을 수 없다.

```python
# 생성
s1 = set([1, 2, 3])
s1 = set()

# 교집합
s1 & s2

# 합집합
s1 | s2

# 차집합
s1 - s2

# 삽입
s1.add(4)
s1.update([4, 5, 6])

# 제거
s1.remove(2)
```

### 함수

```python
# 절댓값 구하기
abs(num)

# 여러 리스트를 순서대로 요소를 뽑을 때
for a, b in zip(a_list, b_list):

# filter 함수
# 특정 조건으로 걸러서 걸러진 요소들로 iterator 객체를 만들어서 반환
# map 함수와 달리 요소의 포함여부를 확인하는 '필터링'
arr = list(filter(lambda x: x % 2 == 0, arr))
  ...

# map 함수
# 반복 가능한 iterable 객체를 받아서, 각 요소에 함수를 적용.
# map(적용할 함수, 적용할 요소들)
result = list(map(lambda x: x+1, arr))

# 값으로 인덱스 찾기
list_data.index("a")

```

### 증감연산자

```python
# 파이썬은 증감연산자가 없다.
i += 1
i -= 1
```

### 문자열

- [문자열 함수 모음](https://github.com/chaeryeon823/Coding-Test/blob/main/Study/StringFunc.md)

### 수학

```python
# 제곱근 구하기
import math
math.sqrt(num)

# 제곱 구하기
import math
math.pow(num)

# 로그
import math
math.log2(num)

# float 유형 숫자가 정수인지 판별
num.is_integer() # boolean 반환

# 진법 변환
# n진수 -> 10진수
int('101',2)

# 10진수 -> 2, 8, 16진수
bin(10)
oct(10)
hex(10)

# 순열(순서있고 중복 없는)
arr = list(permutations(data, 2))

# 조합(순서 상관 없는 경우의 수)
arr = list(combinations(data, 2))
```

### 라이브러리

```python

# 알파벳 리스트 생성
from string import ascii_letters
import ascii_lowercase
import ascii_uppercase

# 날짜와 시간 다루기
import datetime as dt

x = dt.datetime.now()  # 현재 시간을 date클래스 객체로 반환
x.year
x.month
x.day
x.hour
x.minute
x.second
x.microsecond
x.weekday()  # 0부터 월요일

td = dt1 - dt2
td. days
td.seconds, td.microseconds
```

## 1. 자료구조

- [DEQUE](https://github.com/chaeryeon823/Coding-Test/blob/main/Study/DataStructure/Deque.md)
- [Priority Queue](https://github.com/chaeryeon823/Coding-Test/blob/main/Study/DataStructure/PriorityQueue.md)

## 부록. 조각 코드

> 코드를 작성하면서 나중에 필요할 만한 코드

**약수의 합**

```python
answer = num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
```

**약수 배열**

```python
for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
      arr.append(i)
      if (i ** 2) != n:
        arr.append(n // i)
```

**자연수 자리 합**

```python
answer = sum([int(i) for i in str(num)])
```

**행렬 덧셈**

```python
answer = [list(map(sum, zip(*z))) for x in zip(A, B)]
answer = [c + d for c, d in zip(a, b) for a, b in zip(A, B)]
```

**최대공약수 최소공배수**

- [유클리드 호제법](https://github.com/chaeryeon823/Coding-Test/tree/main/Study/Algorithm/Euclidean)
- [[PGS] 12940 최대공약수와 최소공배수](https://github.com/chaeryeon823/Coding-Test/blob/main/PROGRAMMERS/12940.py)
- [[PGS] 12953 N개의 최소공배수](https://github.com/chaeryeon823/Coding-Test/blob/main/PROGRAMMERS/12953.py)

**자리수 출력**

```python
# 1의 자리수만 출력
print(a % 10)

# 1의 자리수만 빼고 출력
print(a // 10)
```

**소수 구하기**

- [에라토스테네스의 체](https://github.com/chaeryeon823/Coding-Test/tree/main/Study/Algorithm/SieveOfEratostenes)

**피보나치 수**

```python
def solution(n):
    answer = 0
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1

    for i in range(1, n):
        a, b = b, a+b

    return a % 1234567
```

- [[PGS] 피보나치 수](https://github.com/chaeryeon823/Coding-Test/blob/main/PROGRAMMERS/12945.py)

**소인수 분해**

```python
def prime_factor(n):
    factors = []
    i = 2
    while i <= n:
      if n % i == 0:
        factors.append(i)
        n = n / i
      else:
        i = i + 1
    return factors
```
