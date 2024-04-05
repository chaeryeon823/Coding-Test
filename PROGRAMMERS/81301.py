# 숫자 문자열과 영단어

def solution(s):
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(en)):
        if en[i] in s:
            s = s.replace(en[i], str(i))
    
    return int(s)
