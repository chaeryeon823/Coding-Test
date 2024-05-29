# 너의 평점은
# s5

import sys

std = {"A+" : 4.5, "A0" : 4.0, "B+": 3.5, "B0": 3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0": 1.0, "F":0}
credit_sum = 0
grade_sum = 0
while True:
	try:
		name, credit, grade = map(str, sys.stdin.readline().split())
		if grade != "P":
			grade_sum += float(credit) * std[grade]
			credit_sum += float(credit)
		else:
			continue
	except:
		break

print(grade_sum / credit_sum)