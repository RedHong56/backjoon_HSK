from collections import deque
#두개 인접까지 허용 "ㅡ" 행 인접 "ㅣ" 열 인접
n, m = map(int, input().split()) #세로 크기 n, 가로 크기 m
graph = [input() for _ in range(n)]


visited = [[False for _ in range(m)]for _ in range(n)]

count = 0

def BFS(y,x):
    global count
    visited[y][x] = True
    dq= deque([(y,x)])

    while dq:
        py, px = dq.popleft()
        if graph[py][px] == "-":
            ny, nx = py, px+1
            if 0<= nx < m and 0<= ny < n:
                if graph[ny][nx]=="-":
                    visited[ny][nx]=True
                    dq.append((ny,nx))
                #     if nx == m-1 :
                #         count += 1 
                # else:
                #     count += 1
                
        if graph[py][px] == "|": # 팝 한 값이 | 일 때
            ny, nx = py+1, px
            if 0<= nx < m and 0<= ny < n:
                if graph[ny][nx]=="|":
                    visited[ny][nx]=True
                    dq.append((ny,nx))
                #     if ny ==n-1:
                #         count += 1 
                # else:
                #     count += 1
                

for i in range(n): #y
    for j in range(m): # x
        if visited[i][j] == False:
            BFS(i,j)
            count += 1
print(count)