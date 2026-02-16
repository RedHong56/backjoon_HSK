def solution(num_list):
    even, odd = 0,0
    for i in num_list:
        if i % 2 :
            odd += 1
        else:
            even += 1
    answer = [even, odd]
    return answer