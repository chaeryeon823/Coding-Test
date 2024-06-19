# 성적표
# 2
# 단순 구현, 딕셔너리

n, m = map(int, input().split())
d = {}
answer = 0
max = 0

for _ in range(n):
	subject_num, score = map(int, input().split())
	
	if subject_num in d.keys():
		d[subject_num].append(score)
	else:
		d[subject_num] = [score]

for key, value in d.items():
	d[key] = sum(value) / len(value)

for key, value in d.items():
	if max < value:
		answer = key
		max = value
	elif max == value:
		if answer > key:
			answer = key

print(answer)
			