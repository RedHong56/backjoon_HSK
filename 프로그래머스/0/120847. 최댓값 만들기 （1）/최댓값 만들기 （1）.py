def solution(numbers):
    sorted_list = sorted(numbers, reverse=True)
    return sorted_list[0] * sorted_list[1]