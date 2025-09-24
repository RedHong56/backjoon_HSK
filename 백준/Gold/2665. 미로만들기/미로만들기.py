import sys
from collections import deque

n = int(sys.stdin.readline()) #8
#인접 정렬
gragh = [list(map(int,sys.stdin.readline().strip()))for _ in range(n)]
# visited = [[False for _ in range(n)]for _ in range(n)]

dm = [(0, 1), (1, 0), (0, -1), (-1, 0)] #상하 좌우 체킹


def bfs():
    # visited[st][st] = True 
    INF = int(1e9)
    dist = [[INF for _ in range(n)]for _ in range(n)]
    dist[0][0] = 0 #첫 시작 지점 초기화
    dq = deque([(0,0)])
    while dq:
        x,y = dq.popleft()
        for dx,dy in dm:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n: #상,하,좌,우 판에서 나가는지 확인

                cost = dist[x][y] + (0 if gragh[nx][ny]==1 else 1)###여기서 부터 중요 다익스트라 핵심
                if cost < dist[nx][ny]: # 테이블에 있는것보다 코스트가 더 적으면
                    dist[nx][ny] = cost # 텓이블에 없데이트 해주고
                    if gragh[nx][ny] == 1: #만약 1이라고 되어있으면
                        dq.appendleft((nx,ny)) #흰방일때 먼저 계산해야 최단거리 보장이됨 #우선순위 heapq 안쓰고 구현
                    else:
                        dq.append((nx,ny))
    return dist[n-1][n-1]
     
print(bfs())
