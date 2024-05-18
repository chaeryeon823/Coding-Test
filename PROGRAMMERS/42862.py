# 체육복
# lv 1
# 그리디

def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n 
    
    for r in reserve:
        arr[r - 1] += 1
    
    for l in lost:
        arr[l - 1] -= 1
    
    for i in range(n):
        if arr[i] == 0:
            if i != 0 and arr[i - 1] == 2:
                arr[i] += 1
                arr[i - 1] -= 1
                continue
            elif i != (n - 1) and arr[i + 1] == 2:
                arr[i] += 1
                arr[i + 1] -= 1
                continue
    
    for a in arr:
        if a >= 1:
            answer += 1
    
    
    return answer