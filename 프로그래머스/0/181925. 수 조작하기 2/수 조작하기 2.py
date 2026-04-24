def solution(numLog):
    answer = ''
    cmd = {1:"w", -1:"s", 10:"d", -10:"a"}
    
    for i in range(1,len(numLog)):
        delta = numLog[i] - numLog[i-1]
        answer += cmd[delta]
        
    return answer

