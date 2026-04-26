def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        
        string = my_strings[i]
        s, e = parts[i]
        
        answer += string[s : e+1]
    return answer