import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline()) # 4<=n<= 100 게임판 크기

arr=[] # [c][l] 행,열
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

#0,0 -> n-1,n-1
#칸에 적혀있는 수만큼
#오른쪽, 아래로만 점프가능

dp = [[0] *(n+1) for _ in range(n+1)]

def jump(i,j): # x, y
    #base
    if i == 0 and j== 0:
        return 1
    if i<0 or j<0:
        return 0
    if i>=n or j>n: #이게 킥임 판 넘어가는거 베이스
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    move = arr[n-i-1][n-j-1] # 0,0부터 읽기
    if move == 0 :
        return 0
    dp[i][j] = jump(i,j-move) + jump(i-move,j)
    return dp[i][j]

print(jump(n-1,n-1))