def solution(babbling):
    lang = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for j in lang:
            i = i.replace(j,' ')
        if i.strip() == '':
            answer += 1
    return answer