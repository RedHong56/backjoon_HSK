import sys
from collections import deque
sys.setrecursionlimit(100_000)

#노드수 / 엣지 수
n,m = map(int, sys.stdin.readline().split())

#연결 요소의 개수 union 그룹 두개 출력

p = [i for i in range(n+1)] #부모 만들기

def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a,b): #부모 합치기
    pa = find(a)
    pb = find(b)
    p[pa]= pb #b부모로 합치는거 아닌가?

arr = []

for i in range(1, m+1):
    node, nodee = map(int, sys.stdin.readline().split())
    union(node, nodee)

for i in range(1, n+1):
    arr.append(find(i))

print(len(set(arr)))