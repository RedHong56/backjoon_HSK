import sys
sys.setrecursionlimit(100_000)
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수
def case():
    N = int(sys.stdin.readline()) #코인 갯수
    coins = list(map(int, sys.stdin.readline().split()))
    cost = int(sys.stdin.readline())
    dp = [[-1] * (cost+1) for _ in range(N)]
    def solv(i, k):
        if k == 0 :
            return 1
        if k<0 or i == N:
            return 0 
        if dp[i][k] != -1:
            return dp[i][k] #중복 호출 해결
        dp[i][k] =solv(i+1, k) + solv(i, k-coins[i])
        return dp[i][k]
    
    print(solv(0, cost))

for _ in range(T):
    case()


###### 바텀 업ㅂ
# import sys
# input = sys.stdin.readline

# T = int(input())  # 테스트 케이스 수

# for _ in range(T):
#     N = int(input())  # 동전 종류 수
#     coins = list(map(int, input().split()))
#     M = int(input())  # 목표 금액

#     dp = [0] * (M + 1)
#     dp[0] = 1  # 0원을 만드는 경우의 수는 1가지

#     for coin in coins:
#         for j in range(coin, M + 1):
#             dp[j] += dp[j - coin]

#     print(dp[M])
