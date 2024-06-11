# 큰 수식 찾기
# 2

# a, b = input().split()
# a = eval(a)
# b = eval(b)

# print(max(a, b))

def cal(s):
	arr = []
	tmp = ''
	check = False
	for c in s:
		# 숫자면
		if c.isdigit():
			tmp += c
		# 숫자가 아니면
		else:
			if check:
				arr.append(str(int(arr.pop()) * int(tmp)))
				tmp = ''
				check = False
			else:
				arr.append(tmp)
				tmp = ''
				
			if c == '*':
				check = True
				continue
			arr.append(c)
					
	if check:
		arr.append(str(int(arr.pop()) * int(tmp)))
	else:
		arr.append(tmp)

	answer = int(arr[0])
	for i in range(1, len(arr) - 1):
		if arr[i] == '+':
			answer += int(arr[i + 1])
		elif arr[i] == '-':
			answer -= int(arr[i + 1])
	
	return answer
				
a, b = input().split()
a = cal(a)
b = cal(b)

print(max(a, b))

