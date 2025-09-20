import sys
sys.setrecursionlimit(100_000)
n, m = map(int, sys.stdin.readline().split())

p= [i for i in range(n+1)] #엄마 n개 만들고
# print(p)

def find(a):
    if a == p[a]:  #엄마 확인해봐
        return a # 엄마 같아? -> 엄마 리턴
    p[a] = find(p[a]) #재귀함수가 돔 #다시 찾아
    return p[a] # 엄마 끝까지 찾아서 리턴

def union(a,b):
    pa = find(a) #너 엄마 찾아봐
    pb = find(b) #b 너도 엄마 찾아봐
    p[pa] = pb    


for _ in range(m):
    cnd, el1, el2 = map(int, sys.stdin.readline().split())

    if cnd == 0: #union
        # print(p)
        union(el1,el2)
        
    else: #find
        if find(el1) == find(el2):
            print("YES")
        else:
            print("NO") 



# # n+1 개의 집합이 있는데 여기서 합집합 연산과 , 두 원소가 같은 집합에 포함되어있는지를 확인하는 연산을 수행하려고 한다.


# # m은 연산으로 주어지는 갯수
# # n = 집합의 수



# # 0 이 주어지면 a,b 를 합친다는 의미 
# # 1 이 주어지면 a,b가 같은 집합인지 확인하는 것
# ass = {}

# for i in range(1, n+1):
#     ass[i] = [i]
# # print(ass)


#     if cnd == 0:
#         ass[el1].append(ass[el2].pop())
#     else:

#         if ass[el1].find(el2):
#             print("YES")
#         else:
#             print("NO")