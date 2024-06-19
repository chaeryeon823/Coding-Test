def solution(s):
    answer = 0
    x= ""
    x_cnt = 0
    nx_cnt = 0

    for c in s:
        if x == "":
          x = c
          x_cnt = 1
          continue

        if c == x:
           x_cnt += 1
        else:
           nx_cnt += 1
          
        if x_cnt == nx_cnt:
           x_cnt = 0
           nx_cnt = 0
           x = ""
           answer += 1

    return answer

a = solution("abracadabra")
print(a)