food = [1, 3, 4, 6]
answer = ''
for i in range(1, len(food)):
    answer += str(i) * (food[i] // 2)
print(answer)
