import sys

n = int(input())

graph = {}

for i in range(n):
    key, val1,val2 = sys.stdin.readline().split()
    graph[key]=(val1,val2)

list_preorder = []
list_inorder = []
list_postorder = []
#preorder
def preorder(node):
    list_preorder.append(node)
    #1. 루트를 삽입하고
    #2. 루트와 간선으로 연결되어있는 노드들을 다시 재귀하며 최종 리프 까지 간다
    if graph[node][0] != '.':
        preorder(graph[node][0])
    if graph[node][1] != '.':
        preorder(graph[node][1]) #기저조건 없어도 되는가?
preorder("A")
print(''.join(map(str,list_preorder)))

#inorder
def inorder(node):
    if graph[node][0] != '.':
        inorder(graph[node][0])
    list_inorder.append(node)
    if graph[node][1] != '.':
        inorder(graph[node][1]) #기저조건 없어도 되는가?
inorder("A")
print(''.join(map(str,list_inorder)))


# postorder 
# 이건 레벨순으로 돌면 될것같은데 어케 하노? ->재귀되는 순서를 노린다?
def postorder(node):
    
    if graph[node][0] != '.':
        postorder(graph[node][0])
    if graph[node][1] != '.':
        postorder(graph[node][1]) #기저조건 없어도 되는가?
    list_postorder.append(node)
    
postorder("A")
print(''.join(map(str,list_postorder)))


