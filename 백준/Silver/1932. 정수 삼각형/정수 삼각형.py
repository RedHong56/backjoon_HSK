import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())  #집의 수
arr = []
for _ in range(n): #탑에서 바텀으로
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*(n+1) for _ in range(n+1)]

def tri(i,j):
    if i<=0:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    
    dp[i][j] = arr[n-i][j] + max(tri(i-1,j),tri(i-1,j+1))

    return dp[i][j]

print(tri(n,0))
