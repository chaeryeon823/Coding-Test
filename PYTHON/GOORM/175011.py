# 0 채우기
# 2
# 배열

n = int(input())
arr = []
answer = 0
for i in range(n):
	tmp = list(map(int, input().split()))
	arr.append(tmp)
	
# 0 찾기
row, col = 0, 0

for i in range(n):
	for j in range(n):
		if arr[i][j] == 0:
			row = i
			col = j
			break

# row 더하기
answer = sum(arr[row])

# col 더하기
answer += sum([arr[i][col] for i in range(n)])


print(answer)