import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stk = []
ans = []

for i in range(n):
    if stk:
        if stk[-1][1] < arr[i]:
            while stk and stk[-1][1] < arr[i]:
                stk.pop()
            if stk:
                ans.append(stk[-1][0])
            else:
                ans.append(0)
            stk.append((i+1, arr[i]))
            
        else:
            ans.append(stk[-1][0])
            stk.append((i+1, arr[i]))
    else: # 어레이가 비어있으면 추가하고  return 0
        ans.append(0)
        stk.append((i+1, arr[i]))

print(" ".join(map(str, ans))) # 9가 읽는게 없음