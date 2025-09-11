TC = int(input())
#채를 한번만 사용 최댓값으로 리스트 생성후 찾아내기
nums = list(int(input()) for _ in range(TC))
max_num = max(nums)

#채 만들기 (이중루프)
prime_num = [True] * (max_num+1) #G
prime_num[0] = False
prime_num[1] = False

for i in range(2, int(max_num**0.5) + 1): #절반의 사이즈에 에라토스테네스
    if not prime_num[i]:
        continue
    for j in range(i * i, max_num + 1, i): # i와 같은 간격인 것들 지워주기 즉 배수 
        prime_num[j] = False  # i*i부터


def determine(n): #nums 리스트 의 인덱스 받기
    a = n // 2 #인덱스의 절반 에서부터 내려오며 탐색하겠다
    while a >= 2: 
        b = n - a # 찾는 인덱스중 남은 값이 
        if prime_num[a] and prime_num[b]: #소수에 포함되면
            print(a, b)       # 차이 최소 쌍
            return
        a -= 1


for i in range(len(nums)):
    determine(nums[i])





# for i in range(2, int(nums[n]/2)+1): # 절반 탐색
#     if prime_num[n] == True and prime_num[nums[n]-i] == True: #찾아야하는 그 수가 소수이면
#         if nums[n]-(i) < (nums[n]-(i-1)):
#             A = i #i값을 저장
# print(f'{A} {nums[n]-A}')




#---------------------------------
# def prime_num(n):
#     arr=[True for i in range(n+1)] # 0부터 ~ n 까지
#     for i in range(2, int(n**(0.5))+1):  # not prime number 판별 복잡도 : 루트 n
#         if not arr[i]:
#             continue
#         for j in range(i * 2, len(arr), i):
#             arr[j] = False
#     #arr에 T, F 값으로 정리

#     A = 0
#     B = 0

#     for i in range (2, int(len(arr)/2)+1): #arr 1부터 절반까지 확인
#             if arr[i] ==True:
#                 for j in range(int(len(arr)/2),len(arr)): # 절반부터 n까지 인덱스 확인
#                     if arr[j]==True and i+j== n :
#                         A=i
#                         B=j

#     print(f'{A} {B}')



# for i in range(0,int(TC)):
#      prime_num(int(input()))

