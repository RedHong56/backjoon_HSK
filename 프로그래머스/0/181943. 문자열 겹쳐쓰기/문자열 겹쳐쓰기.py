def solution(my_string, overwrite_string, s):
    # s 전까지 + 덮어쓸 문자열 + 덮어쓴 이후의 남은 문자열
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

print(solution)