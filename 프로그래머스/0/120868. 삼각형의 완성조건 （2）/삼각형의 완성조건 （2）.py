def solution(sides):
    answer = 0
    max_side = max(sides)
    sum_side = sum(sides)
    sub_side = sum_side - max_side
    
    # 다른 한 변 = 가장 긴 변
    answer = sum_side - max_side
    
    # 주어진 값 max = 가장 긴 변
    for i in range(max_side):
        if sub_side + i > max_side:
            answer += 1
    
    return answer