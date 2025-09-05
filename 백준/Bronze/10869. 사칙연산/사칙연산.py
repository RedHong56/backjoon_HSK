# A, B = map(int, input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)


# map() 각 원소를 변환하는 기능
C, D = map(int, input()) #input: 35
print(C) # 3
print(D) # 5
print(type(C))
print(type(D))

#.split() 문자열을 토막내서 리스트로 만드는 기능
text = "apple banana cherry"
print(text)
testsplit = text.split()   # 공백 기준으로 자르기
print(testsplit)
print(text.split())

