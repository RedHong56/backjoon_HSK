import sys

n = int(sys.stdin.readline())
stk = []
for _ in range(n):
    a = int(sys.stdin.readline())

    if a==0:
        stk.pop() if stk else -1
    else: stk.append(a)

print(sum(stk))