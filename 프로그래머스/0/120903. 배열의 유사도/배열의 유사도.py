def solution(s1, s2):
    answer = 0
    for i in s1:
        if s2.count(i):
            answer += 1
    return answer