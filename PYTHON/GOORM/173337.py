# 8진수 계산기
# 2

N = int(input())
arr = list(map(int, input().split()))
print(oct(sum(arr))[2:])