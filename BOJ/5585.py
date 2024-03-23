# 거스름 돈

import sys

coins = [500, 100, 50, 10, 5, 1]
answer = 0

n = int(sys.stdin.readline().rstrip())
money = 1000 - n

for coin in coins:
  answer += money // coin
  money = money % coin

print(answer)