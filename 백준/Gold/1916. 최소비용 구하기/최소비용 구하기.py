import sys
from collections import deque
import heapq
#-------------다익스트라-----------------
#노드의 개수(도시)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

gragh = {i: [] for i in range(n+1)}
visited = [False for _ in range(n+1)]
ans = []
for _ in range(m):
    #도시 도시 가중치
    a,b,w = map(int, sys.stdin.readline().split())
    gragh[a].append((b,w))


start, desti = map(int, sys.stdin.readline().split())

#거리 초기화
INF = int(1e9) #무한대 10의 9승으로 설정
distance = [INF] * (n+1) #노드 수만큼 거리를 정해두고
distance[start] = 0 # 시작 노드 거리 기록

#우선순위 큐
pq = [] #priority
heapq.heappush(pq, (0,start))

while pq:
    dist, now = heapq.heappop(pq) #가장 작은 우선순위 배출
    if dist> distance[now]: #더 멀면
        continue # 다음 루프로 넘겨 버린다

    for nxt,w in gragh[now]: #노드와 인접원소들을 순차적으로 확인
        cost = dist + w # 코스트는 현재 노드에 가중치를 더한값
        if cost < distance[nxt]: #만약 그 코스트가 지금 테이블에 있는것보다 작으면
            distance[nxt] = cost #테이블을 업데이트 해주고
            # print(distance)
            heapq.heappush(pq, (cost, nxt)) #힙 푸쉬해주기

if distance[desti]==INF:
    print(-1)
else:
    print(distance[desti])