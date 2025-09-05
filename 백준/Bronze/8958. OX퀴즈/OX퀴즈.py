'''문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.'''
#1. O가 몇 번 연속인가?
#2. sum 으로 사용

number_of_test = int(input())
test=[] # 테스트케이스
test_score = 0 #연속으로 맞출때 올라가는 점수
sum= 0 # 최종 점수

for i in range(number_of_test): # 1, 2, 3, 4, 5 ... 문제 열기
    test.append(input()) #문제들 추가 하기
# print(test)

for i in range(number_of_test):
    for j in range(len(test[i])): #len: list의 요소 갯수 (끝 인덱스의 번호 X)
        if test[i][j] =='O':
            test_score +=1
        elif test[i][j] =='X': 
            test_score = 0
        # print(test_score)
        sum+=test_score
    
    test_score = 0
    print(sum)
    sum = 0

# A = ['123456789', '987654321']
# print(len(A[1]))
# print(A[1][4]) # 문자열에서 찾기
# 숫자배열에선 어케함? 형변환 해야할듯?
# print(Test)