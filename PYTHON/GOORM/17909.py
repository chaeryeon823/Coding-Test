# 카드모으기
# 2

n, m = map(int, input().split())
answer = -1
arr = set()

for i in range(m):
	num = int(input())
	if num not in arr:
		arr.add(num)
	
	if len(arr) == n:
		answer = i + 1
		break


print(answer)


# set은 append로 삽입하는게 아니라 add 임
# set자료형의 in 연산은 O(1)로 빠름 따라 이렇게 체킹해야하는 상황에서 고민해보기.