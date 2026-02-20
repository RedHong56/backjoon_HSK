def solution(s):
    answer = 0
    lastest = 0
    
    s = s.split(' ')
    
    for i in s:
        if i == 'Z':
            answer -= lastest
        else:
            val = int(i)
            answer += val
            lastest = val
            
    return answer