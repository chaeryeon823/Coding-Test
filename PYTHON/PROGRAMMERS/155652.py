# 둘 만의 암호
# lv1
# 97 ~ 122
def solution(s, skip, index):
    answer = ''
    cnt = 0
    for c in s:
        tmp = ord(c)
        while cnt < index:
            tmp = tmp + 1
            if tmp > 122:
                tmp = (tmp - 122) + 96
            if chr(tmp) not in list(skip):
                cnt += 1

        cnt = 0
        print(chr(tmp))
        answer += chr(tmp)
                
            
    return answer

print(solution("aukks",	"wbqd",	5))