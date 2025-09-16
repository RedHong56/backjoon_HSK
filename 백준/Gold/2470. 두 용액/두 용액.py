import sys

n = int(sys.stdin.readline())

fluid = list(map(int, sys.stdin.readline().split()))
fluid.sort()

left = 0 # 음수중 가장 작은 것
right = len(fluid)-1 #양수중 가장 큰 것
a = fluid[0]
b = fluid[len(fluid) - 1]

best = abs( a+ b) #최초 갱신


while left < right:
    # 양 쪽 끝의 값을 더했을때 절댓값이 0에 가까워 져야함
    mix = fluid[left] + fluid[right]

    if best > abs(mix) :
        best = abs(mix)
        a = fluid[left]
        b = fluid[right]
    
    else: 
        if mix > 0:         #1. 0 초과
            right -= 1 #len -2
        elif mix < 0:        #2. 0 미만
            left += 1 #0+1
        else: break

        #3. 다른 조합이 0과 더 가까울때 abs 절대값 사용

print(f"{a} {b}")