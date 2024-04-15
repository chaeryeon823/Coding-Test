# 실패율

def solution(N, stages):
    answer = []
    arr = [0 for i in range(N + 1)]
    dict = {}
    
    tmp = len(stages)
    
    for i in range(N):
        cnt = stages.count(i + 1)
        if cnt != 0:
            dict[i + 1] = cnt / tmp
            tmp = tmp - cnt
        else:
            dict[i + 1] = 0

    answer = sorted(dict, key=lambda x:-dict[x])
    return answer