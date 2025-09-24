import sys
from collections import deque
n ,m = map(int, sys.stdin.readline().split())
#위상절렬은 방향성이 있다
gragh = {i: [] for i in range(n+1)}
# 진입 차수 배열 만들기
dgree =[0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    # 노드별로 들어오는 간선 개수 세기
    dgree[b] +=1
ans = []

# 큐 초기화
dq = deque()
# 진입 차수가 0인 노드들을 큐에 넣기
for i in range(1,len(dgree)):
    if dgree[i] == 0:
        dq.append(i)
# 반복 (while 큐)
while dq:
    np =dq.popleft()
    # 큐에서 노드 꺼내서 결과 리스트에 추가
    ans.append(np)
    # 해당 노드와 연결된 간선 제거 → 연결된 노드 진입 차수 -1
    for nxt in gragh[np]:
        dgree[nxt] -= 1
        if dgree[nxt] == 0:
            dq.append(nxt)

    # 만약 진입 차수가 0이 되면 큐에 추가

# 결과 출력
print(" ".join(map(str,ans)))