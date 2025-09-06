# # 개선된 소수 판별 함수
N= int(input())

tc = list(map(int, input().split()))

count = 0
sum = 0
divide = 0

for i in range(0,N): #테스트 케이스 루프
    root = int((tc[i])**(1/2)) # 아파테이아의 채? 활용한 루트 (공배수 찾기용)
    for j in range(2,root+1):
        divide += 1
        if tc[i]%j == 0: continue 
        if tc[i]%j != 0:
            sum+=1 
    if(sum==divide and int(tc[i])>1):
        count += 1
    sum=0
    divide =0

print(count)
