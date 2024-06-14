# 고장난 컴퓨터
# 1
# 구현

import sys
n, c = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

answer = 1

for i in range(1, n):
	if t[i] - t[i - 1] >= c + 1:
		answer = 1
	else:
		answer += 1

print(answer)