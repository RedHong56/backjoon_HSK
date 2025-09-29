import sys
sys.setrecursionlimit(100_000)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
DP = [[-1]*(n+1) for _ in range(n+1)]

# min 사용
def procession(i,j): #왼쪽, 오른쪽 
    if DP[i][j] != -1 :
        return DP[i][j]
    if  i==j:
        return 0
    ans = 1e9

    for mid in range(i, j):
        # print(f"{procession(i,mid) + procession(mid+1,j) + arr[i][0] * arr[mid][1] * arr[j][1]}, i: {i} j : {j}")
        # print(f"left: {procession(i,mid)}  right:{procession(mid+1,j)}")
        if ans > procession(i,mid) + procession(mid+1,j) + arr[i][0] * arr[mid][1] * arr[j][1] :
            ans = procession(i,mid) + procession(mid+1,j) + arr[i][0] * arr[mid][1] * arr[j][1]
        
    
    DP[i][j] = ans
   
    return DP[i][j]

print(procession(0,n-1))


#1. 겹치는 부분중 왼 ,오 선택 하는게
#2. 만약 n 이라면
#3. 그 n은  ((n-2)*(n-1))*n 과 (n-2)*((n-1)*n) 중 선택해서 넣기
    #이걸 배열로 풀어 쓰면 두개 씩 나온다 각 조합에서
    # 다시 말해서 항이 3개라면 2개중 하나를 비교하고
    # 항이 4개라면 경우의 수가 3개
    # 항이 5개 라면 경우의 수가
#4. 이게 점화식인가?
    #제일 작은거 * 가장 작은거
    # if arr[i-1][0] < arr[i+1][1]:
    #     dp[i][j] = (arr[i-1][0]*arr[i][0]*arr[i][1])   + (arr[i-1][0]*arr[i][1]*arr[i+1][1])
    # else:
    #     dp[i][j] = (arr[i+1][0]*arr[i+1][1]*arr[i][0]) + (arr[i-1][0]*arr[i][0]*arr[i+1][1])
    # return dp[i][j]

    # 왼쪽의 [0][1] 오른쪽[0][1]

    #왼쪽 [0] * 중간 [0][1] + 왼쪽 [0] * 중 [1] * 오 [0]
    #오른쪽 [1] *  중간[0][1] + 오른 [1]* 중간 [0] * 왼쪽 [0]