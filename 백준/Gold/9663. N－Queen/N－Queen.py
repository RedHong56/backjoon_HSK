n = int(input()) # 입력 값

pos = [0] * n #각 열에서 퀸의 위치를 출력
flag_a = [False] * n #각 행에 퀸을 배치했는지 체크
flag_b = [False] * (2*n-1) #대각선 1,3 사분면 방향 체크
flag_c = [False] * (2*n-1) # 대각선 2,4 사분면 방향 체크

count = 0

def put() -> None:
    global count
    count += 1
    # for i in range(n):
    #     print(f'{pos[i]}',end=' ')
    # print()


# i = 열 j = 행
def set(i: int) -> None: #열에 퀸을 배치 
    for j in range(n): # 행 8개 중 어디 놓지?
        if(  not flag_a[j]  #행 트루에서 false고
            and not flag_b[i+j] #우상 좌하 대각선에서도 false고
            and not flag_c[i-j + (n-1)] ): # 좌상 우하 대각선에서도 false면
            pos[i] = j # 현재 놓으려는 열의 행을 선택
            if i == (n-1): #들어온 값이 마지막 7열이라면 종료 (기지조건)
                put()
            else:
                flag_a[j] = flag_b [i + j] = flag_c[i - j + (n-1)] = True #가로와 
                set(i + 1) # 다음열 퀸 배치
                flag_a[j] = flag_b [i + j] = flag_c[i- j + (n-1)] = False


set(0)
print(count)
#분할 정복법 큰 문제를 작은 문제로 분할하고, 작은 문제 풀이법을 결합하여 전체 풀이법을 얻는 방법
# 작은 문제 풀이법에서 원래의 문제 풀이법을 쉡ㄱ 할 수 있도록 설계

#기지조건 더이상 쪼개지지안음


# def set(i: int) -> None: #열에 퀸을 배치

#     for j in range(8): #행 8개 중
#         if not flag[j]: # 행에 플래그가 false 이면
#             pos[i] = j # 현재 놓으려는 열의 행을 선택
#             if i == 7: #들어온 값이 마지막 7열이라면 종료
#                 put()
#             else:
#                 flag[j] =True
#                 set(i+1) #다음 열에 퀸을 배치
#                 flag[j]=False