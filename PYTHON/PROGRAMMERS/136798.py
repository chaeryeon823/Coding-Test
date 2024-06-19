# 기사단원의 무기
# lv 1

import math

def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        attack = 0
        for i in range(1, int(n**(1/2)) + 1):
            if n % i == 0:
                attack += 1
                if (i ** 2) != n:
                    attack += 1
            
            if attack > limit:
                attack = power
                break
        
        answer += attack
        
    return answer