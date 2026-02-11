def solution(a, b):
    a = str(a) 
    b = str(b)
    if(int(a+b)>int(b+a)):
        answer = a+b
    else:
        answer = b+a
    return int(answer)