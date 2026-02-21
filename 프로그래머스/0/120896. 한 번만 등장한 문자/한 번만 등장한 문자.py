def solution(s):
    answer = ''
    
    for i in range(97,123) :
        if s.count(chr(i)) == 1 :
            answer += chr(i)
    
    return answer