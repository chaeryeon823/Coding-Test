def solution(n, m, section):
    answer = 1
    check = section[0]

    for s in section:
        if s >= check + m:
            check = s
            answer += 1
    
    return answer


