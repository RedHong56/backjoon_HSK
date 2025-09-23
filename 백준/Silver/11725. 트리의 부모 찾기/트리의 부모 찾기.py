import sys
from collections import deque
sys.setrecursionlimit(100_000_000)

n = int(sys.stdin.readline()) #노드의 개수
e = n-1 #간선의 개수

gragh = {i:[] for i in range(n+1)} # 노드 만들기
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a)

#방문자
visited = [False for _ in range(n+1)]
parent = [0] * (n+1)

def find(start):
    visited[start] = True

    for i in gragh[start]: #들어오는 노드 값의 인접원소들 loop
        if not visited[i]: #일단 방문했는가?
            parent[i]= start #인접노드의 부모 설정
            find(i)
find(1)

for i in range(2, len(parent)):
    print(parent[i])
# 출력은 2번 노드 부터 바로 위에 있는 부모님 찾기
