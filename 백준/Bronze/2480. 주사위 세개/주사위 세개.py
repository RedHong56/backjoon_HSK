a, b, c = map(int,input().split())

if a == b == c:
    print(10000 + 1000*a)
elif a != b and a != c and b != c:
    print(100*max(a,b,c))
else:
    double = 0
    if a == b:
        double = a
    elif a == c:
        double = a
    else:
        double = c
    print(1000 + 100*double)