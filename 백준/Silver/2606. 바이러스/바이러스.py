import sys
from collections import deque
#인접하고 있는 감염된 컴퓨터 수

#노드의 갯수
n = int(sys.stdin.readline())
#엣지의 갯수
e = int(sys.stdin.readline())

gragh = {i : [] for i in range(n+1)}

#엣지 연결
for _ in range(e): 
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a)

# 방문체크
visited = [False for _ in range(n+1)]


def bfs(start):
    count = 0

    visited[start] = True #첫 시작점 방문체크
    queue = deque([start])

    while queue: #다 넣었다 빼면 스탑
        node= queue.popleft() #처음꺼 빼주고

       
        for nxt in gragh[node]:
            if not visited[nxt] :
                count+=1
                queue.append(nxt)
                visited[nxt] = True
    return count

print(bfs(1))

    
        