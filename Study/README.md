## 0. 코딩테스트 파이썬 필수 문법

### 입력

```
# 정수
n = int(sys.stdin.readline().rstrip())

# 한줄에 여러 변수
n, m, k = map(int, sys.stdin.redline().split())

# 리스트
data = list(map(int, sys.stdin.redline().split())

# 문자열 리스트
plan = sys.stdin.readline().split()
```

### 정렬

```
# 정렬하기
data.sort()

# 2차원 배열 정렬하기
data.sort(key = lambda x:(x[1], x[0]))
```

### 함수

```
# 리스트에서 가장 큰 수 찾기
value = max(data)

# 리스트에서 가장 작은 수 찾기
value = min(data)

# 리스트 크기 구하기
len(data)
```

### 증감연산자

```
# 파이썬은 증감연산자가 없다.
i += 1
i -= 1
```

### 자리수 출력

```
# 1의 자리수만 출력
print(a % 10)

# 1의 자리수만 빼고 출력
print(a // 10)
```
