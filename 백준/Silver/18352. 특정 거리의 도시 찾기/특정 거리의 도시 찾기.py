import sys
from collections import deque
#x까지 최단거리가 정확히 k인 모든 도시들의 번호를 출력 단, x to x는 0이다
#n 노드 , m arc, k 거리정보, x 출발 도시
n, m, k, x = map(int, sys.stdin.readline().split())

gragh = {i: [] for i in range(n+1)}
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)

#큐에 넣었다 뺏다하는 행위를 생각해서 몇번 넣었는지 카운트 하면 되지않을까?

visited = [False for _ in range(n+1)] #방문자 만들기
ans = []

def bfs(distance, start):
    # 첫 시작 노드 큐에 넣기
    queue = deque([ (distance,start) ])
    visited[start] = True

    while queue:
        dd,dn = queue.popleft() #팝
        if dd == k :
            ans.append(dn)

        for node in gragh[dn]:
            if not visited[node]:    
                visited[node] = True #방문
                nd = dd+1 #거리를 계속 갱신해줘야함
                queue.append((nd, node)) #큐에 인접 노드들 넣어줬고

bfs(0,x)

ans.sort()
if ans:
    for i in ans:
            print(i)
else: print(-1)