def solution(a, b):
    ax, bx = a%2, b%2
    x= ax+bx
    
    if x == 2 :
        return a**2 + b**2
    elif x == 1 :
        return 2*(a+b)
    else:
        return abs(a-b)
        