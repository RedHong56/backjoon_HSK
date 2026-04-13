students = [False] * 30

for _ in range(28):
    call = int(input())
    students[call-1] =True

for i in range(30):
    if students[i] == False:
        print(i+1)