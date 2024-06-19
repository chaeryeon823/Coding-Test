from collections import Counter

# 신고 결과 받기
# lv 1

def solution(id_list, report, k):
    answer = []
    dic = {}
    
    for i in id_list:
        dic[i] = [0, 0]
    
    set_report = set(report)
    
    for r in set_report:
        a, b = r.split()
        dic[b][0] += 1
        
    for r in set_report:
        a, b = r.split()
        if dic[b][0] >= k:
            dic[a][1] += 1
    
    answer = [tmp[1] for tmp in dic.values()]
    return answer