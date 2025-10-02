import sys

n = int(sys.stdin.readline())

#2원 , 5원으로만 거스름

if n==1 or n==3:
    print(-1)
else:
    if (n%5) %2 == 0: #짝수일때
        five_rtn = n%5
        five = n//5
        two = five_rtn//2
        print(five+two)

    else:   #홀수일때
        five_rtn = (n%5)+5
        five = (n//5)-1

        two = five_rtn//2
        print(five+two)