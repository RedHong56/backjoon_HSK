import sys
stk = []
n = int(sys.stdin.readline())
large = 0

for _ in range(n):
    a= int(sys.stdin.readline())
    if stk :
        if large <= a: # 다 가릴정도로 큰수가 들어오면 클리어 시키기
            large = a
            stk.clear()
            stk.append(a)
        else: #그게 아니라면 top과 비교하여 append 처리하기
            if stk[-1] > a:
                stk.append(a)
            elif stk[-1] < a:
                while stk[-1]<=a:
                    stk.pop()
                stk.append(a)
                

    else:  # 비어있을때 넣기
        stk.append(a)
        large = a



print(len(set(stk)))