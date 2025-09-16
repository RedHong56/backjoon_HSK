import sys
from collections import deque
n= (int(sys.stdin.readline()))
que = deque(range(1,n+1))
# 1~ n 까지 카드가 있고
# 가장위에 1 밑에 n
while len(que)>1:
#1. 위에 카드버리고
    que.popleft()
    que.append(que[0])
    que.popleft()

print(que[0])
#2. 가장 위에 있는 카드는 아래로 -> 원형 큐? 링버퍼?
