# 유클리드 호제법

> [최대공약수(GCD), 최소공배수(LCM) 구하기 유클리드 호제법 알고리즘 :: 코드자몽](https://myjamong.tistory.com/138)  
> [최대 공약수(GCD) 알고리즘 - 유클리드 호제법](https://heoseongh.github.io/algorithm/Euclidean/)

## Euclidean Algorithm - GCD(Greatest Common Divisor)

- 두 개의 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘
- 두 자연수 A, B (A > B)에 대하여 A를 B로 나눈 나머지를 R이라고 할 때, A, B의 최대 공약수는 B와 R의 최대공약수와 같다.
- 이 성질에 따라 B를 R로 나눈 나머지 R0를 구하고, 다시 R을 R0로 나눈 나머지 R을 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 A와 B의 최대공약수이다.

> GCD(15, 12) = GCD(12, 15 % 12) = GCD(12, 3)  
> GCD(3, 12) = GCD(3, 12 % 3) = GCD(3, 0)

```python
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def gcd(a, b):
  if a % b == 0:
    return b
  return gcd(b, a % b)

```

- 2개의 자연수를 받아 최대 공약수를 받기 위해 1부터 두 자연수 중 작은 자연수까지 모두 나누어 보면서 가장 큰 공약수를 구할 수 있다.
- 위의 방식은 O(N)의 시간 복잡도를 가지고, 유클리드 호제법 알고리즘을 사용하면 시간 복잡도는 O(logN)이 된다.

---

## Euclidean Algorithm - LCM(Least Common Multiple)

- 최소공배수는 두 자연수의 곱을 최대공약수를 나누면 계산할 수 있다.

```python
def lcm(a, b):
  return a * b / gcd(a, b)
```

---
