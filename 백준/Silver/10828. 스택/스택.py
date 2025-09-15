import sys
stk = [] # 스택 리스트

n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push":
        stk.append(int(cmd[1]))
        


    elif cmd[0] == "size":
        print(len(stk))

    elif cmd[0] == "empty": #비었으면 1 아니면 0 출력
        print( 0 if stk else 1) #stk가 있으면 0 아니면 1 출력

    elif cmd[0] == "top": #스택이 비었을때 인덱스 에러 조건 필요
        print(stk[-1] if stk else -1) #stk -1 을 출력하는데 아니면 -1을출력
        
    elif cmd[0] == "pop": #비었을때 인덱스 에러 조건필요
        print(stk.pop() if stk else -1)
        