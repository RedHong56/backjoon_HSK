def solution(my_string):
    answer = []
    for i in my_string :
        if ord(i) < 96 :
            answer.append(int(i))
    return sorted(answer)