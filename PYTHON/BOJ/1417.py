# 국회의원 선거
import sys, heapq

n = int(sys.stdin.readline().rstrip())
winner = -int(sys.stdin.readline().rstrip())
candidate = []
answer = 0

for i in range(n-1):
  tmp = int(sys.stdin.readline().rstrip())
  heapq.heappush(candidate, -tmp)

if candidate:
  while winner >= candidate[0]:
    max_candidate = heapq.heappop(candidate)
    heapq.heappush(candidate, max_candidate + 1)
    winner -= 1
    answer += 1

print(answer)
