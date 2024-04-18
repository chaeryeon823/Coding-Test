# [1차] 다트 게임

import math
def solution(dartResult):
    bonus = {"S":1, "D":2, "T":3}
    score = [0, 0, 0]
    index = 0
    tmp = ""
    for c in dartResult:
        if c.isdigit():
            tmp += c
        
        elif c in bonus.keys():
            score[index] = math.pow(int(tmp), bonus[c])
            index += 1
            tmp = ""
        elif c == "#":
            score[index - 1] = score[index - 1] * -1
        else:
            if index - 2 > -1:
                score[index - 2] *= 2
            score[index - 1] *= 2

    return sum(score)



# import re


# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer