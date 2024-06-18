# 햄버거 만들기
# lv 1

def solution(ingredient):
    tmp = []
    answer = 0
    std = [1, 2, 3, 1]
    
    for i in range(len(ingredient)):
        tmp.append(ingredient[i])
        print(tmp[-4:])
        if tmp[-4:] == std:
            answer += 1
            for _ in range(4):
                tmp.pop()
    return answer

# 흠.. join으로 했을 때, 실패가 돼서 확인하니
# replace가 한번에 모든 1231을 바꾸어서 그런것
# 그래서 replace의 count를 변경하니 시간초과
# 정공법으로 문제 설명처럼 하나씩 주입하여 했더니 성공..