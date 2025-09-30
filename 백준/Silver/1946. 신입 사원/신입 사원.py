import sys
tc = int(sys.stdin.readline())
for _ in range (tc):
    n = int(sys.stdin.readline())
    arr= []
    for _ in range(n):
        a,b = map(int, sys.stdin.readline().split())
        arr.append([a,b])

    arr.sort(key= lambda x: (x[0]))
    count = 0
    t = 1e9
    for employee in arr:
        r = employee[1]
        if r<t:
            t = r
            count +=1
    print(count)