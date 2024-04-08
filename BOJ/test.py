answer = [1,2,3,4,5]
cnt = [0, 0, 0]
s1 = [1, 2, 3, 4, 5]
s2 = [1, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

for i in range(len(answer)):
    if s2[i % len(s2)] == answer[i]:
        print("같음!!  answer", i)

print(cnt)
