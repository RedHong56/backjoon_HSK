# 후위표기식
import sys
stk = []
n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().strip() # 개행 '\n' 같이 들어옴
    ok = True
    
    for i in a:
        if i == "(":
            stk.append("(")

        elif i==")"  : 
            if stk :
                stk.pop()
            else: ok=False # 중간 체크용
            
    # (가 없어서 비어있는 상태일수도 있음 중간 체크 필요

    if len(stk)==0 and ok:
        print("YES")
    else: print("NO")

    stk.clear()



