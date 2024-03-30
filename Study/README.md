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

### 리스트

```python
# 리스트 정렬하기
data.sort()

# 2차원 리스트 정렬하기
data.sort(reverse=True)

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
```

### 함수

```python
# 절댓값 구하기
abs(num)
```

### 증감연산자

```python
# 파이썬은 증감연산자가 없다.
i += 1
i -= 1
```

### 자리수 출력

```python
# 1의 자리수만 출력
print(a % 10)

# 1의 자리수만 빼고 출력
print(a // 10)
```

### 문자열

```python
# 문자열에서 문자 치환
text.replace('a', 'b', [바꿀 횟수])

# 문자열에서 특정 문자 개수 세기
text.count('a')

# 문자열 소문자로 전환
text.lower()

# 문자열 대문자로 전환
text.upper()s
```

### 수학

```python
# 제곱근 구하기
import math
math.sqrt(num)

# 제곱 구하기
import math
math.pow(num)

# float 유형 숫자가 정수인지 판별
num.is_integer() # boolean 반환
```

### 라이브러리

```python

# 알파벳 리스트 생성
from string import ascii_letters
import ascii_lowercase
import ascii_uppercase

```

## 1. 자료구조

### 우선순위 큐

> 우선순위 큐(heapq, priority Queue)  
> https://velog.io/@mein-figur/Python%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-heapq  
> https://velog.io/@hsshin0602/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90priority-%ED%9E%99%ED%81%90heap  
> https://chunsubyeong.tistory.com/88

파이썬으로 우선순위 큐를 구현하는 방법은 PriorityQueue, heapq가 있다. 파이썬은 우선순위 큐 모델인 PriorityQueue를 제공한다.
하지만 heapq가 더 빠르기 때문에 시간 초과가 나지 않기 위해 heapq를 사용하는 것을 지향한다. (이유는 위에 링크 참조)

**PriorityQueue**

```python
from queue import PriorityQueue

q = PriorityQueue()
q = PriorityQueue(maxsize=10) # 크기 제한

# 원소 삽입
q.put(3)
q.put(4)
q.put(1)

q1.put((1, 'apple')) # (우선순위, 값)의 형태로 저장할 수도 있음


# 원소 삭제
q.get() # 1
q1.get()[1] # (우선순위, 값)의 형태에서 값 반환
```

<br>

**heapq**

```python
import heapq

# 힙 선언 방식
# 빈 배열로 초기화 하여 선언 하거나 선형 배열을 heapify를 통해 힙으로 변형

hq = []
hq1 = [1, 2, 3]
heapq.heapify(arr)

# 원소 삽입
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)

# 원소 삭제
heapq.heappop(hq)

# 힙은 기본적으로 최소힙으로 구현되어 있다. 따라 최대힙으로 변형하기 위해선 다음과 같은 방법으로 해야한다.
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap)

# [(-9,9), (-7,7), (-5,5), (-3,3), (-1,1)]

# 이때 실제 원소의 값은 튜플의 두번째 자리에 저장되어 있다.

max_item = heapq.heappop(max_heap)[1]

```

- [[BOJ 1715] 카드정렬하기 / G4](https://github.com/chaeryeon823/Coding-Test/blob/main/BOJ/1715.py)

- [[BOJ 11000] 강의실 배정 / G5](https://github.com/chaeryeon823/Coding-Test/blob/main/BOJ/11000.py)

- [[BOJ 1927] 최소힙 / ](https://github.com/chaeryeon823/Coding-Test/blob/main/BOJ/1927.py)

## 부록. 조각 코드

> 코드를 작성하면서 나중에 필요할 만한 코드

**약수의 합**

```python
answer = num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
```

**자연수 자리 합**

```python
answer = sum([int(i) for i in str(num)])
```
