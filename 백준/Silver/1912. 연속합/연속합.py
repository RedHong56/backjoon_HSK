import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [0] * (n)

def sequence_sum(i):
    if i<0:
        return 0
    if dp[i] != 0:
        return dp[i]
    dp[i] = arr[i]
    dp[i] = max(dp[i], sequence_sum(i-1)+dp[i])

    return dp[i]



print(max(sequence_sum(i) for i in range(n))) #뒤에있는걸 땡겨주는
