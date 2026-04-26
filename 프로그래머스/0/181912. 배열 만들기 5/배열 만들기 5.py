def solution(intStrs, k, s, l):
    answer = []
    
    for string in intStrs :
        temp = int(string[s : s+l])
        
        if temp > k :
            answer.append(temp)
    
    return answer