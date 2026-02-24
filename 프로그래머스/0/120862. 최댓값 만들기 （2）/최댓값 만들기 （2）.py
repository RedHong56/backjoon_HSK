def solution(numbers):
    numbers.sort()
    
    nega = numbers[0] * numbers[1]
    posi = numbers[-1] * numbers[-2]
    
    return max(nega,posi)