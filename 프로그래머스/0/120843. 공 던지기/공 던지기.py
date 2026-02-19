def solution(numbers, k):
    throw_index = (k-1) * 2
    
    while throw_index > len(numbers) :
        throw_index -= len(numbers)
        
    return numbers[throw_index]