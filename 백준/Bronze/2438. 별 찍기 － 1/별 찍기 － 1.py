'''첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제'''
N=int(input())
for i in range(1, N+1): print(i*'*',end='\n')
#반복 i 초기화 주의