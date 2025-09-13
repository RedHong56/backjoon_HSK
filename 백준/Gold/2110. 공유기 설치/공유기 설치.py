import sys
hou, ip = map(int, sys.stdin.readline().split())
address = list([int(input()) for _  in range(hou)])
address.sort() #리스트 정렬

#1. 처음 주소를 기점으로 간격을 이분 탐색하며  ip 갯수만큼 존재하는지 알아내기

high= address[-1]-address[0] # 최대 간격
low = 1 # 주소간의 최소 간격 why?  간격의 중간 값을 구하기 위해
ans = 0

while low<=high: 
    count = 1
    mid = (high+low) //2 #간격의 중간 값
    point = address[0] # 간격을 세기 시작하는 첫번째 지점

    for i in range(1, len(address)): #첫번째 포인트부터 확인하겠다
        if address[i]-point >= mid: #간격보다 이상일 때
            point = address[i] # ip 설치를 다시 해주고
            # print(point)
            
            count += 1 #설치후 갯수 세기
    if count >= ip: #세는게 공유기 수를 넘어가면 일단 갱신 공유기 설치 갯수 많으면 간격을 넓혀야함
        ans = mid

        # print(ans)

        low = mid + 1
    else: #공유기 설치 갯수가 적으면 간격을 좁혀야함
        high = mid - 1

print(ans)