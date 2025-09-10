# N, r, c = map(int, input().split())


def Z(n, r, c):
    if n==0:
        return 0 

    half = int(2**n/2) #한 변의 절반 크기
    area = half*half # 그 사이즈의 크기

    quad = 0 # 이 값이 0: 좌상 / 1: 우상 /  2: 좌하 / 3: 우하
    if r>=half:
        quad +=2 
        r -= half #영점 이동

    if c >= half:
        quad += 1
        c -= half #영점 이동
    
    return quad * area + Z(n-1, r, c)


a,s,d = map(int, input().split())

print(Z(a,s,d))
# N, r, c = map(int, input().split())


# N = 1
# r = 0
# c = 1

# square = [True]*(2**N)*(2**N) # 스퀘어라는 리스트 생성
# def Z(a: int):
#     rows = 2**a
#     step = int(rows/2)

#     if square[0] == True: # 아직 좌상이 켜져있을때
#         Z(step) # 다시 더 작게 재귀함수 호출
#         square[0] = False
#     else: #좌상이 false 일때
#         if square[i+step] : # 우상이 true 일때
#             Z(0+step) #기저 돌리고
#             square[0+step]=False
#         else: #좌상 우상이 false 일때
#             if square[(rows*step)]:
#                 Z(rows*step)
#                 square[(rows*step)]=False
#             else:  #좌하가 false 일때
#                     if square[(rows*step)+step]:
#                         Z((rows*step)+step)
#                         square[(rows*step)]=False

# Z(N)
