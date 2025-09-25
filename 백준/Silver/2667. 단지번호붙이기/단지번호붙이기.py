import sys
from collections import deque
# 3주차 시험 2
# 단지 번호 붙이기

#BFS 와 큐를 사용하여
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip()))  for _ in range(n)]
dm = [(0,1), (0,-1), (1,0), (-1,0)]
visited =[[False for _ in range(n)]for _ in range(n)]
ans = []

def BFS(y, x):
    dq = deque([(y,x)])
    count = 1

    while dq:
        py,px= dq.popleft()
        visited[py][px]= True

        for i in dm:
            ny,nx = py+i[0], px+i[1]
            if 0<=ny<n and 0<=nx<n:
                nc = graph[ny][nx]
                if nc == 1 and not visited[ny][nx] :
                    visited[ny][nx]= True
                    dq.append((ny,nx))
                    count += 1
            # print(dq)
    return ans.append(count)


for i in range(n):
    for j in range(n):
        if graph[i][j]== 1 and not visited[i][j]:
            BFS(i,j)
                

print(len(ans))
ans.sort()
for i in ans:
    print(i)



#플래그를 0 1 2 3을 세우면되는데
# 0에서 시작해서 1을 만나면 1이 되고

# 다시 0에서 1을 만나면 2가됨

# 이때 1에서 1을 만나면 1이여야함

# 0에서 0을 만나도 그거임