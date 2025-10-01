import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
count_fib = 0
count_fibonacci = 0

# def fib(n):
#     global count_fib
    
#     if n==1 or n==2:
#         return 1
#     else:
#         count_fib +=1
#         return(fib(n-1)+ fib(n-2))
    
dp =[-1] * (n+1)
dp[1] = 1
dp[2] = 1
def fibonacci(n):
    global count_fibonacci
    if dp[n] != -1:
        return dp[n]
    if n<0:
        return 0
    dp[n] = fibonacci(n-1)+fibonacci(n-2)
    count_fibonacci += 1
    return dp[n]


print(fibonacci(n), count_fibonacci)
