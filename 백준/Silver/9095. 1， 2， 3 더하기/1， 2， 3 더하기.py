n = int(input())
arr = [int(input()) for _ in range(n)]


point = 0
def roll(x:int):
    global point
    if x==0:
        point += 1
    elif x<0 : return 0

    roll(x-1), roll(x-2), roll(x-3)

for i in arr:
    roll(i)
    print(point)
    point = 0