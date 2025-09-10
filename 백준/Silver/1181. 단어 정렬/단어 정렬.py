import sys

n= int(sys.stdin.readline().strip('\n')) # 입력이 많을때 빨리 읽는법 정수니 int로

arr = set(input() for _ in range(n)) # 중복 제거하기

arr = list(arr)

sorted_words = sorted(arr, key=lambda x:(len(x), x)) # sorted 원소들을 정렬해서 새로운 리스트를 만든다
#정렬할 때 기준(key)를 lambda 함수로 정한다.


for i in range(len(sorted_words)):
    print(sorted_words[i])


#복합 정렬 : multi-ket sort 여러 조건을 동시에 적용하는 정렬 방식
# key lambda: 한 줄짜리 익명 함수 키워드
# 튜플이 자동적으로 사전적 비교를 해줌