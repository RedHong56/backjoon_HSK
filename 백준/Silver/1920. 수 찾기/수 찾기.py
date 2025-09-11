import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
A.sort()

def binary(arr:list, target:int): #arr 는 찾는 범위 target은 찾는 value
    
    start = 0
    end = len(arr)-1 #len -1


    while start<=end:
        mid = (start +end) //2
        if arr[mid] == target:
            return 1
        elif target>arr[mid]:
            start = mid + 1

        elif target < arr[mid]:
            end = mid - 1

    return 0


for i in H:
    print(binary(A,i))
    
#이진 탐색
# 1. j를 절반에서 찾는다
# 2. 안나오면 +- 절반
# 3. len이 1이 되면
# 4. 이진 탐색 안됨 => 정렬 안되있음 sort()사용
# 5. 아웃 풋은 M과 관련 된 것들