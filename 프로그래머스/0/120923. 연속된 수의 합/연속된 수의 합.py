def solution(num, total):
    answer = []
    
    avg = total//num + (1 if total%num else 0)
    
    first = avg - num//2 
    last = avg + num//2 + (0 if total%num else 1)
    
    for i in range(first, last):
        answer.append(i)
    
    return answer