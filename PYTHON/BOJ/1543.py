# 문서 검색
# s5

import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

s1 = s1.replace(s2, '*')

print(s1.count('*'))