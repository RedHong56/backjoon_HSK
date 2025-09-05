#윤년:  4의 배수(o) 100의 배수(x) 400의 배수 (o) 윤년이면 return:1 아니면 0
year=int(input())
if (year%400)==0 : print(1)
elif (year%100)==0 : print(0)
elif (year%4==0) : print(1)
else: print(0)
