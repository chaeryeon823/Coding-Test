# 제로
# S4

import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
  tmp = int(sys.stdin.readline().rstrip())

  if tmp != 0:
    arr.append(tmp)
  else:
    arr.pop()

print(sum(arr))
