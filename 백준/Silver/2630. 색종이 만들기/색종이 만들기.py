N = int(input())

paper = [list(map(int, input().split() ))for _ in range(N)]
white = 0
blue = 0


def color(x:int, y:int, size):
    global white,blue
    if size < 1:
        return
    
    half = size//2
    base = paper[y][x] #y축에서 선택 , x축에서 선택 (색 탐색용)
    #우선 쪼개기전 전체 색칠 되어있는지 확인
    for i in range(y, y+size): # 세로
        for j in range(x, x+size): #가로

            if paper[i][j] != base: #베이스랑 다르면 4분할 ㄱㄱ
                color(x, y, half) #1사분면
                color(x+half, y , half) #2사분면 세로 변화 x , 가로 변화 0
                color(x, y+half, half) #3사분면 t세로변화 o 가로 변화 x               
                color(x+half, y+half, half) # 4사분면
                return
    
    if base == 0:
        white+=1
    else: 
        blue +=1 
    return

color(0,0,N)
print(white)
print(blue)