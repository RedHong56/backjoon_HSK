import sys
sys.setrecursionlimit(100000)
tc = int(sys.stdin.readline())

for _ in range(tc):

    n = int(input()) 
    dp = [0] * (101)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    def tri(a):

        for i in range(5,a+1):
            dp[i] = dp[i-1] + dp [i-5]
        return dp[a]
    print(tri(n))

