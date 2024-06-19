money = int(input())
changes = [1, 50, 10, 20, 40]
answer = 0

for change in changes:
	tmp = money // change
	answer += tmp
	money -= (change * tmp)
	print(money)

	
print(answer)