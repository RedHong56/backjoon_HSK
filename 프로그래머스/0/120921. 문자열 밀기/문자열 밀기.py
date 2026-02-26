def solution(A, B):
    if A == B:
        return 0
        
    for i in range(1, len(A)):
        order = A[-i:] + A[:-i]
        if order == B:
            return i
            
    return -1