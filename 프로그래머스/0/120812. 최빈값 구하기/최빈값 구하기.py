def solution(array):
    count_arr = [0] * 1000 
    for i in array:
        count_arr[i] += 1
    
    max_count = max(count_arr)
    
    if count_arr.count(max_count) > 1:
        return -1
    
    return count_arr.index(max_count)