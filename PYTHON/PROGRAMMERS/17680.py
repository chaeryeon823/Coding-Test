# [1차] 캐시
# lv 2
# LRU

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        else:
            cache.popleft()
            cache.append(city)
            answer += 5
    return answer