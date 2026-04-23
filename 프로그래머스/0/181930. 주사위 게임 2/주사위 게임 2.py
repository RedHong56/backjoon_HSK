def solution(a, b, c):
    num = set([a,b,c])
    if len(num) == 3 :
        return a + b + c
    elif len(num) == 2 :
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)