import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())  #집의 수
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
# print(arr)
dp = [[-1] * 3 for _ in range(n)]

#min
def color(i, j): #j는 색 정보
    if dp[i][j] != -1:
        return dp[i][j]
    #붙어 있는 양옆에 있는 집의 색이 달라야함
    if i == 0:
        dp[i][j] = arr[0][j]
    else:
        #for 문과 if 문을 따로 쓰면 이터러블로 인식 x
        dp[i][j] =arr[i][j] + min(color(i-1, k) for k in range(3) if k != j) 
        
    return dp[i][j]
print(min(color(n-1, i) for i in range(3)))

