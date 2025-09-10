n = int(input())

Q= [list(map(int, input().split())) for _ in range(n)]

for i in range(len(Q)):
    student_total= sum(Q[i][1:])/Q[i][0]

    big_student = 0

    for j in Q[i][1:]:
        if student_total<j:
            big_student += 1

    ans=big_student/Q[i][0]*100

    print(format(ans,'.3f'),end="%\n")

