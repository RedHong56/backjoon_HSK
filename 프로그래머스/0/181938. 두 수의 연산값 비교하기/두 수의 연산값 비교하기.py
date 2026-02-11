def solution(a, b):
    if(int(f"{a}{b}") >= 2*a*b):
        answer = int(f"{a}{b}")
    else:
        answer = 2*a*b
    return answer