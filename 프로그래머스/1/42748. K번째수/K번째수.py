def solution(array, commands):
    answer = []
    for cmd in commands:
        first = cmd[0] - 1  
        last = cmd[1]       
        find_idx = cmd[2] - 1
        
        srt = sorted(array[first:last]) 
        answer.append(srt[find_idx])
        
    return answer