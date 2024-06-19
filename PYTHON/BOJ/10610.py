# 30
# s4
# 수학
# 배수 판정법, 3의 배수는 각 자리 수의 합이 3의 배수이다.

import sys

N = sys.stdin.readline().rstrip()

if '0' in N:
    tmp = sum(map(int, list(N)))
    if tmp % 3 != 0:
        print(-1)
    
    else:
        answer = ''.join(sorted(list(N), reverse=True))
        print(answer)
else:
    print(-1)


# 수학 문제는 한번 접근하기 어렵다.. 흑흑