
def move(n,x,y) -> None :

    if n>0:
        move((n-1), x , 6-x-y)
        print(f'{x} {y}')

    if n>0:
        move((n-1), 6-x-y , y)
    # print(x,y) # 여기들어오면 n=0, n=1 쯤 문제가 생김

k = int(input())

print(2**k -1)
if k <= 20:
    move(k, 1 , 3)


