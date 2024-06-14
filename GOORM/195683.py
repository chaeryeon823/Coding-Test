# 운동 중독 플레이어
# 1
# 수학


import math
w, r = map(int, input().split())
answer = w * (1 + r / 30)
print(math.floor(answer))