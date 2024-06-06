# DNA 비밀번호
# s3

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
s = sys.stdin.readline().rstrip()
# A G C T
rule = list(map(int, sys.stdin.readline().split()))
answer = 0
# 부분 문자열 만들기
for i in range((n - m) + 1):


print(answer)
