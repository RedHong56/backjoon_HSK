import sys
sys.setrecursionlimit(100_000)
n, k = map(int, sys.stdin.readline().split())
arr = [int(input()) for _ in range(n)]
count = 0

for coin in range(len(arr)-1,-1,-1):
    if k == 0:
        break
    elif k < arr[coin]:
        pass
    else:
        m=k//arr[coin]
        k -= m * arr[coin]
        count += m
    

print(count)