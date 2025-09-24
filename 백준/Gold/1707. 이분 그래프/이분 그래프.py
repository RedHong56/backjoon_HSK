# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 
# 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 
import sys
sys.setrecursionlimit(100_000)
#tc 갯수

k = int(sys.stdin.readline())

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    grafh = {i: [] for i in range(v+1)}
    for _ in range(e):
        a,b = map(int, sys.stdin.readline().split())
        grafh[a].append(b)
        grafh[b].append(a)

    color = [0] * (v+1) #color 0: 방문 안함 1 ,-1로 구분하기

    def dfs(start, c):
        color[start] = c #들어온 값으로 셋팅    
        for i in grafh[start]:
            if color[i] == 0: #방문 안했던 노드
                if not dfs(i,-c): #반대 색으로 색칠
                    return False #이부분 잘이해 안됨
            elif color[i] == c: # 색상이 같을때
                return False
        return True
        
    ok = True
    for i in range(1,v+1):
        if color[i]==0: # 다 초기화 되있는지 확인
            if not dfs(i, 1):
                ok= False
                break
    print("YES" if ok else "NO")