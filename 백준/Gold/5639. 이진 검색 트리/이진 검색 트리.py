import sys
sys.setrecursionlimit(10**6) 
# GPT 힌트: pre 와 post의 성질을 이용해라

arr = []
#전위 순회 리스트 만들기
for line in sys.stdin:
    arr.append(int(line.strip()))


def post(start, end): #루트가 될 노드를 기준으로
    #기저조건
    if start > end: 
        return
    # 첫 값 루트를 기준으로 l, r 가르기
    root = arr[start]
    #root 기준으로 작은 값
    idx = start + 1 #루트 빼고 시작하는 값
    while idx <= end and arr[idx] < root: #루트 보다 커지는 인덱스를 구하기 위해서
        idx += 1
    post(start+1 , idx-1)  # 작은쪽
    post(idx, end) #큰쪽
    print(root)
        
        
post(0, len(arr)-1)

# 루트 값 변경해서 재귀
# 재귀 무한 반복하다가 len = 1일때 베이스 케이스





#후위 순회 아웃풋 뽑기
#어떻게 만들것인가? 주어지는 갯수 n도 주어지지 않는다
#트리를 만든 조건을 활용해서 트리를 만들어 볼까ㅏ?
    #1. 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다
    #2. 노드의 오른쪽 서브트리에 있는 모드 노드의 키는 노드의 키보다 크다
    #3. 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다. 2진이기에 반씩 나누는게 좋을지도?

# 제일 위에 있는 노드는? 첫값을 기준으로?
# key , value 분배 어케함?




# sys.setrecursionlimit(10**6) 
# def insert(node, value):
#     if node not in tree: #트리에 노드 없으면 노드 생성
#         tree[node] = [None,None]
#     if value < node: # 들어온 값이 노드보다 작을때 왼쪽 자식으로
#         if tree[node][0] is None: #자식이 비어있을때 삽입하고 자식 만들기
#             tree[node][0] = value
#             tree[value] = [None,None]
#         else: # 자식 있을때 재귀함수 드가자~
#             insert(tree[node][0], value)
#     else: #들어온 값이 노드보다 클때 오른쪽 자식으로
#         if tree[node][1] is None:
#             tree[node][1] = value
#             tree[value] = [None,None]
#         else: # 자식 있을때 재귀함수 드가자~
#             insert(tree[node][1], value)

# tree = {}
# nd = int(sys.stdin.readline())
# for line in sys.stdin: 
#     insert(nd, int(line.strip()))
# # print(tree[nd][0])

# def search(pt): #키 값임
#     if tree[pt][0] != None:
#         search(tree[pt][0])

#     if tree[pt][1] != None:
#         search(tree[pt][1])

#     print(pt)

# search(nd)
