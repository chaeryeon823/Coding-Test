# 꽃 선물하기
# 1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
flower_type = ['Sunflower', 'Tulip', 'Rose']
answer = []

for i in range(N):
	a, b = map(int, input().split())
	if a < b:
		answer.append(flower_type[0])
	elif a == b:
		answer.append(flower_type[1])
	else:
		answer.append(flower_type[2])

for a in answer:
	print(a)
