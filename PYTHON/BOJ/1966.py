# 프린터 큐
# S3

import sys
from collections import deque

test_case = int(sys.stdin.readline().rstrip())

for t in range(test_case):
  n, f = map(int, sys.stdin.readline().split())

  q = deque(map(int, sys.stdin.readline().split()))
  cnt = 0

  while q:
    best = max(q)
    

