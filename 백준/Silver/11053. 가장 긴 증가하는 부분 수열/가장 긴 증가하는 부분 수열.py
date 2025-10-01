import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1] * n

def lis(i):
    # arr[i]를 마지막 원소로 하는 LIS 길이
    if dp[i] != -1: # 이게 반복문 스탑하게 해줌
        return dp[i]
    dp[i] = 1  # 자기 자신만 있을 때 길이 1
    for j in range(i):  # 0 ~ i-1 중에서
        if arr[j] < arr[i]:   # 오름차순 조건
            dp[i] = max(dp[i], lis(j) + 1)
    return dp[i]

ans = 0
for i in range(n):
    ans = max(ans, lis(i)) #모든 위치 확인하는 것
print(ans)