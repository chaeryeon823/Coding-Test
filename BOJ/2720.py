# 세탁소에 사장 동혁
import sys

coins = [25, 10, 5, 1]
n = int(sys.stdin.readline().rstrip())

for t in range(n):
  pay = int(sys.stdin.readline().rstrip())
  answer = [0, 0, 0, 0]
  for i in range(len(coins)):
    answer[i] += pay // coins[i]
    pay = pay % coins[i]
  
  print(answer[0], answer[1], answer[2], answer[3])

