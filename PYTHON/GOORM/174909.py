# M배 배열
# 2
# 배열

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
	if arr[i] % m != 0:
		arr[i] = arr[i] * m
		
print(*arr)