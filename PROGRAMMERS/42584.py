# 주식 가격
# lv 2

from collections import deque

def solution(prices):
    answer = []
    d = deque(prices)
    while d:
        tmp = d.popleft()
        time = 0
        for n in d:
            time += 1
            if n < tmp:
                break
        
        answer.append(time)

    return answer