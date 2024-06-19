# 연속 부분 수열 합의 개수
# lv 2
# 구현

def solution(elements):
    arr = []
    l = len(elements)
    for i in range(l):
        for j in range(l - 1):
            arr.append(sum(elements[i:i + j + 1]))
        elements.append(elements[i])
    
    arr = set(arr)
    return len(arr) + 1
