# 문자열
# s4
# 부르트포스, 문자열

import sys
a, b = sys.stdin.readline().split()
arr = [0] * ((len(b) - len(a)) + 1)
for i in range(len(b) - len(a) + 1):
    tmp = b[i:i+len(a)]
    for j in range(len(a)):
        if tmp[j] != a[j]:
            arr[i] += 1

print(min(arr))