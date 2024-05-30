# 접미사 배열
# s4
# 문자열

import sys

s = sys.stdin.readline().rstrip()
arr = []

for i in range(len(s)):
  arr.append(s[i:])

arr.sort()

for a in arr:
  print(a)