# 수열
# 2

K = int(input())
a, b = 0, 1

for i in range(1, K):
	a, b = b, a + b

print(a % 1000000007)

# 피보나치