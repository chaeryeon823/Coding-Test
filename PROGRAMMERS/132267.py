a = 3
b = 1
n = 20

answer = []
while n >= a:
  tmp = n // a
  answer.append(tmp * b)
  n = n - (tmp * a) + (tmp * b)

print(answer)