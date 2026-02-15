def solution(money):
    coffee_num = money//5500
    answer = [coffee_num, money - (5500 * coffee_num)]
    return answer