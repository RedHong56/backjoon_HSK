for loop in range(int(input())): 
    sum=0
    big=0
    A= list(map(int, input().split())) #map 이해
    for i in range(1,len(A)):
        sum += A[i]
    avg=sum/A[0]
    for i in range(1,len(A)):
        if avg<A[i]:
            big+=1
    num= big/A[0]
    print(format(num*100,'.3f'),end='%\n') # 포매팅
