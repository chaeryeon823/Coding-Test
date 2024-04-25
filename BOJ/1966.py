# 프린터 큐
# S3

import queue, sys

q = queue()
test_case = int(sys.stdin.readline().rstrip())

for t in range(test_case):
  n, find = map(int, sys.stdin.readline().split())
  