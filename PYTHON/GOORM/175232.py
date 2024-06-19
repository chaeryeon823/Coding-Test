# 숫자 배열
# 2

N = int(input())
s = ''
for i in range(1, (N * N) + 1):
	s += str(i) + ' '
	if i % N == 0:
		print(s[:-1])
		s = ''