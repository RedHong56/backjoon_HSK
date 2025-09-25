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
