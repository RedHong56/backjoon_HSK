n = int(input())

def fivonacci(a):
    arr = [0] * (a+1)
    arr[0] = 0
    arr[1] = 1
    i = 2
    while arr[a] == 0:
        arr[i]= arr[i-1]+arr[i-2]
        i += 1

    return arr[a]



print(fivonacci(n))


#--------------------------------
#DP Top- down
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    arr = [0] * (n+1)
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

n = int(input())
print(fibonacci(n))
################
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 늘리기 (큰 n 대비)

memo = {0: 0, 1: 1}  # 이미 아는 값 저장

def fib(n):
    # 이미 계산된 값이 있으면 바로 반환
    if n in memo:
        return memo[n]
    # 없으면 재귀로 구해서 memo에 저장
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

n = int(input())
print(fib(n))





#----------------------------------
#DP Bottom-up
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, curr = 0, 1  # arr[0]=0, arr[1]=1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

n = int(input())
print(fibonacci(n))
