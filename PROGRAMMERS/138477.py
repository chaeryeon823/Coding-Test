# 명예의 전당 (1)

import heapq

k = 3
score = [10, 100, 20, 150, 1, 100, 200]

answer = []
rank = []
for s in score:
    if len(rank) < k:
        heapq.heappush(rank, s)
    else:
        min_rank = heapq.heappop(rank)
        heapq.heappush(rank, max(min_rank, s))
        
    answer.append(rank[0]) 

print(answer)