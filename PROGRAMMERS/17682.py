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