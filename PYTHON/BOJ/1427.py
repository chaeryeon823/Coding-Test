# 소트인사이드
# s5

import sys

num = sys.stdin.readline().rstrip()
arr = list(num)
arr.sort(reverse=True)
answer = ''.join(arr)
print(answer)