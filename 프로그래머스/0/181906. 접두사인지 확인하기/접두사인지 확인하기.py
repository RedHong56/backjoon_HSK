def solution(my_string, is_prefix):
    leng = len(is_prefix)
    return int(my_string[:leng] == is_prefix)