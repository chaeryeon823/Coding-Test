# H-Index
# lv 2
def solution(citations):
    answer = 0
    arr = sorted(citations, reverse = True)
    
    for idx in range(len(arr)):
        if (idx + 1) <= arr[idx]:
            answer = idx + 1
        else:
            return answer
        
print(solution([3, 4]))