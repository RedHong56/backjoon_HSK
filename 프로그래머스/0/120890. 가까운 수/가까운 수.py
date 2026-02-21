def solution(array, n):
    array.sort()
    dst_arr = []
    
    for i in array:
        distance = abs (i-n)
        if distance > abs(n-i):
            distance = abs(n-i)
        dst_arr.append(distance)
    
    return array[dst_arr.index(min(dst_arr))]