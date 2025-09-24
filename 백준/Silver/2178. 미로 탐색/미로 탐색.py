import sys
from collections import deque
dm = [(1,0),(0,1),(-1,0),(0,-1)] #상,하,좌,우
x, y = map(int, sys.stdin.readline().split())
#인접행렬로 접근
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(x)]
visited = [[0]*y for _ in range(x)]


def bfs(a:int,b:int) :
    queue = deque([(a,b)])
    visited[a][b] = 1 # 첫방문 정보 바꿔주기
    while queue : 
        cx, cy = queue.popleft() #왜 a,b 가 아니냐 반복하면서 계속 바뀌기때문에

        for dx,dy in dm: #상하좌우반복 돌리며 확인
            #팝한값과 상, 하, 좌,우 더하고
            nx = cx + dx 
            ny = cy + dy
            if  0 <= nx < x and 0 <= ny < y : #범위내 값인지 확인
                    if arr[nx][ny]==1 and visited[nx][ny] == 0: #방문했는지, 길인지 확인
                        visited[nx][ny] = visited[cx][cy] + 1 # 
                        queue.append((nx,ny))
                        
    return visited[x-1][y-1] #기록하는거구나
print(bfs(0,0))