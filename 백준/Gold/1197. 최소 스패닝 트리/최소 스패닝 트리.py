import sys
sys.setrecursionlimit(100_000)
# vertex / e = edge
v, e = map(int, sys.stdin.readline().split())
#부모
p = [i for i in range(v+1)]
#트리 만들기
tree = []
for _ in range(e):
    a, b, h = map(int, sys.stdin.readline().split()) #파스칼 알고리즘을 쓰려면 저장해야함?
    tree.append([h, a, b])
tree.sort() #가중치에 맞게 정렬

def find(a):
    if a == p[a]: #초기 설정이어도 탈출, 끝까지 찾아가도 탈출
        return a
    p[a] = find(p[a])
    return p[a]

def union(a,b): # 같은 부모 만들기
    pa = find(a) 
    pb = find(b)
    p[pa] = pb

sum = 0 #가중치 합산
for i in tree:
    #부모 맞춰주고
    aa = find(i[1])
    bb = find(i[2])
    if  aa!=bb :
        sum += i[0]
        union(i[1], i[2])

print(sum)