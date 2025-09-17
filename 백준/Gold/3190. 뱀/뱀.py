import sys
from collections import deque
n = int(sys.stdin.readline())

board = [[True]*n for _ in range(n)] #for in range 해야지 서로 다른 객체를 참조함
#y 값은 board를 n으로 나누었을때 나오는 몫 
#x 값은 몫에서 부터 0~5

k = int(sys.stdin.readline())

for _ in range(k):
    app_x, app_y = map(int, sys.stdin.readline().split())
    board[app_x-1][app_y-1] = False

#뱀은 1 cm 이며 처음에는 0,0 에서 오른쪽인 0,1을 향한다
snake = deque()
snake.appendleft([0,0])
angle = 0 # 0 , 90 , 180 ,270 에 따라 변경
count = 0

m = int(sys.stdin.readline()) # 방향 전환 시간
posi = [list(sys.stdin.readline().split())for _ in range(m)]
i = 0

while True: 
    count +=1 # 시간 카운트
    
    #각도에 따라 머리위치
    if angle == 0:
        new = ([snake[0][0] , snake[0][1]+1])
    elif angle == 90:
        new = ([snake[0][0]-1 , snake[0][1]])
    elif angle== 180:
        new = ([snake[0][0] , snake[0][1]-1])
    else: #angle==270
        new = ([snake[0][0]+1 , snake[0][1]])

    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0<=new[0]<n and 0<=new[1]<n) :    
        break 

    if new in snake:
        break
    
    #부딪히는지 확인하고 머리추가     # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    snake.appendleft(new)

    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    if board[(new[0])][(new[1])]:
        snake.pop()
    else: #다음 머리 위치
        board[(new[0])][(new[1])] = True # 이거 GPT 사과 먹고 바꾸기

    #방향전환 초 비교
    if count == int(posi[i][0]):
        if posi[i][1] == "D":
            angle+=270
        else: # L 일때
            angle += 90
        angle = angle % 360
        if i < m-1: i += 1

print(count)

#방향 디버깅
#사과 먹고 초기화 
#추가하고자하는거 체크