# 베스트셀러

# import sys
# from collections import Counter

# N = int(sys.stdin.readline().rstrip())
# arr = []
# bestseller = []
# for i in range(N):
#     arr.append(sys.stdin.readline().rstrip())

# c = Counter(arr)
# most_cnt = max(c.values())
# c = c.items()

# for i in c:
#     if i[1] == most_cnt:
#         bestseller.append(i[0])

# bestseller.sort()
# print(bestseller[0])

import sys

n = int(sys.stdin.readline().rstrip())
books = {}

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    if tmp not in books.keys():
        books[tmp] = 1
    else:
        books[tmp] += 1

max_cnt = max(books.values())
bestseller = []
for key, value in books.items():
    if value == max_cnt:
        bestseller.append(key)

bestseller.sort()
print(bestseller[0])
