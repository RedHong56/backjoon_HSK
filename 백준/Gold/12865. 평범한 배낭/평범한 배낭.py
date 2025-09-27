import sys
sys.setrecursionlimit(100_000)
input = sys.stdin.readline

#물품 수, 들수있는 무게
item, weight = map(int,input().split())
bag = [list(map( int, input().split())) for _ in range(item)]
bag.sort()
bag.reverse()
# print(bag)
dp = [[0] * (weight+1) for _ in range(item+1)] #dp = 4*7 물건 무게 + 물건 가치

def dpr(i,w):
    if w <= 0 or i < 0:
        return 0
    if dp[i][w] != 0:
        return dp[i][w]
    #물건 가치를 더해 그게 맥스 일때 뱉으면 되는거아님?
    if w >= bag[i][0]:  #이게 '킥'임 넣을수 있는지 없는지 판단 
        dp[i][w] = max( dpr(i-1,w) ,dpr(i-1 , w-bag[i][0] ) + bag[i][1])

    return dp[i][w]
print(dpr(item-1,weight))

# print(dp)