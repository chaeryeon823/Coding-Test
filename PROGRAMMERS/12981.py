# 영어 끝말잇기
# lv 2

def solution(n, words):
    answer = [0, 0]
    last = words[0][-1]
    
    for i in range(1, len(words)):
        if last != words[i][0] or words[i] in words[0:i]:
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
        else:
            last = words[i][-1]
        
    
    return answer
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))