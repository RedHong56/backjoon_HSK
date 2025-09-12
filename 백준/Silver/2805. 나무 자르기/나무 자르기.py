import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 결정(타겟이 명확할때), 최적화()
# 어퍼 바운드

def H(a:list,target:int):
    big = max(a) #  max() 원리 이해 하면 좋을듯    
    start,end = 0 , big # 큰 나무 길이 기준
    ans = 0
    while start<=end: # 이진탐색 조건

        total = 0 #나무들의 총 합 (target이랑 비교)
        mid = (start+end)//2 # 자르는 중간점

        # print(f"start{start} / mid {mid} / end{end}")
        for i in a: #자르는 포인트보다 큰 경우
            if i > mid :
                total += (i-mid)

        if total >= target: #여기가 upper냐 lower 냐 구분점
            ans = mid # 여기가 킥
            start = mid + 1  # 잘랐는데 나무가 많아 -> 더 올려 잘라야지
        else:
            end = mid - 1 # 나무가 적어 -> 

    return ans
print(H(trees, M))




# #---------------import bisect------------------
# print(bisect.bisect_left(arr, x))   # lower_bound → 2가 처음 나오는 위치 (index 1)
# print(bisect.bisect_right(arr, x))  # upper_bound → 2보다 큰 값(3)이 처음 나오는 위치 (index 3)
#등호의 차이

# # X 이상의 첫위치
# def lower_bound(arr, x):
#     lo, hi = 0, len(arr)
#     while lo < hi:
#         mid = (lo + hi) // 2

#         if arr[mid] < x:   # x보다 작은 건 버려도 됨
#             lo = mid + 1
#         else:              # arr[mid] >= x → 후보
#             hi = mid
#     return lo  # x 이상 첫 위치

# # X 초과 첫 위치
# def upper_bound(arr, x):
#     lo, hi = 0, len(arr)
#     while lo < hi:
#         mid = (lo + hi) // 2

#         if arr[mid] <= x:  # x 이하 값은 버려도 됨 
#             lo = mid + 1
#         else:              # arr[mid] > x → 후보
#             hi = mid
#     return lo  # x 초과 첫 위치


# a = [ 1,2,3,5,65,67,466]

# print(upper_bound(a,65)) #인덱스 값 출력
# print(lower_bound(a,65))