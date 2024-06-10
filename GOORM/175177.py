# 거스름 돈
# 2

money = int(input())
changes = [40, 20, 10, 5, 1]
answer = 0

for change in changes:
	tmp = money // change
	answer += tmp
	money -= (change * tmp)

print(answer)
	