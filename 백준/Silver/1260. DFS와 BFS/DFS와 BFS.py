import sys
from collections import deque
#node / edge / start node
n, m, v = map(int, sys.stdin.readline().split())

 #노드갯수에 맞춰 인접 리스트 만들기
gragh = {i: []for i in range(1, n+1)}
for _ in range(m): 
    a, b = map(int, sys.stdin.readline().split())
    gragh[a].append(b)
    gragh[b].append(a) #이렇게 해야지 무방향 그래프가 됨


#체크리스트 만들기
visited_dfs = [False for _ in range(n+1)]

arr_dfs = []
#DFS 출력
def dfs(node):
    gragh[node].sort() #백준같은 경우 정렬이 필요할 수 있음
    if visited_dfs[node] == False:
        arr_dfs.append(node)
        visited_dfs[node] = True
        for i in gragh[node]:
            dfs(i)
    #담는거 부터
dfs(v)
print(" ".join(map(str, arr_dfs)))

#BFS 출력
arr_bfs = [] 
visited_bfs = [False for _ in range(n+1)]
def bfs(node):
    queue = deque([node])
    visited_bfs[node]=True #들어오는 값 체크해주기

    while queue:
        search = queue.popleft()
        arr_bfs.append(search)

        for nxt in gragh[search]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)
bfs(v)
print(" ".join(map(str, arr_bfs)))

#    1
#   / \
#  2   3
# / \   \
# 4  5   6

# 1 → 2 → 4 → (백트랙) → 5 → (백트랙) → 3 → 6
# [1]
# [1,2]
# [1,2,4] → 4 끝 → pop
# [1,2,5] → 5 끝 → pop
# [1,3]
# [1,3,6] → 6 끝 → pop

# 1 → 2 → 3 → 4 → 5 → 6
# 큐: [1]
# → 1 꺼냄, 2·3 추가 → [2,3]
# → 2 꺼냄, 4·5 추가 → [3,4,5]
# → 3 꺼냄, 6 추가   → [4,5,6]
# → 4 꺼냄 → [5,6]
# → 5 꺼냄 → [6]