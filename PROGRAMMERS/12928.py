# 약수의 합

import sys

n = int(sys.stdin.readline().rstrip())

answer = 0

if n > 1:
  answer = 1
  for i in range(2, n//2 + 1):
    if n % i == 0:
      answer += i
  answer += n

elif n == 1:
  answer = 1
print(answer)