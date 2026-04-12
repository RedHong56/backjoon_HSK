def solution(citations):
    citations.sort()
    answer = 0

    for i in range(len(citations)):
        h = len(citations) - i
        
        if citations[i] >= h:
            return h
    
    return answer