# 소수 찾기

import math
n = 17
answer = 0
arr = [True] * (n + 1)

arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        for j in range(i + i, n + 1, i):
            arr[j] = False

print([i for i in range(2, )])