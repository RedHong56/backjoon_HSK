def solution(array):
    # 정렬
    array.sort()
    mid = len(array) // 2 # len = 홀수
            
    return array[mid]