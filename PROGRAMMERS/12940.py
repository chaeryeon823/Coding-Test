# 최대공약수와 최소공배수

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(n, m):
    g = gcd(n, m)
    l = n * m / g
    
    return [g, l]

# def solution(n, m):
#     answer = []
#     arr = []
#     for i in range(1, min(n, m) + 1):
#         if n % i == 0 and m % i == 0: 
            
#             arr.append(i)
#     for i in range(max(n, m), (n * m) + 1):
#         if i % n == 0 and i % m == 0:
#             min_num = i
#             break
#     max_num = max(arr)
#     answer.append(max_num)
#     answer.append(min_num)
#     return answer