# 구름 스퀘어
# 2

N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
data.sort(key = lambda x: (x[1], x[0]))
answer = 1

end_time = data[0][1] + 1

for i in range(1, N):
	if data[i][0] >= end_time:
		answer += 1
		end_time = data[i][1] + 1

print(answer)

# 백준 회의실 배정이랑 똑같