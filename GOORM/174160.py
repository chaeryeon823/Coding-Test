# 단어 필터
# 2
# 문자열

empty_message = 'EMPTY'

n, m = map(int, input().split())
s = input()
e = input()

while True:
	if s in e:
		e = e.replace(s, '')
	else:
		break

if e == '':
	print(empty_message)
else:
	print(e)