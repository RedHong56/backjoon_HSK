import sys

a,b,c = map(int, sys.stdin.readline().split())
# print(a,b,c)
t = 1
def remain(x:int,y:int,z:int):
    #(x**y) * (x**y//2) *  (x**y//4 * x**y//4) 이런식으로

    if y==1:   #기저 조건 y가 1이 되면 종료
        return x%z # 결합
    
    elif y%2 == 0 : # 지수가 짝수 일때
        divide = remain(x,y//2,z) # 지수의 절반으로 재귀 (정복)
        return (divide*divide) % z # 결합
    
    else: # 지수 홀수 일때
        divide = remain(x,y//2,z) # 지수의 절반으로 재귀 (정복)
        return (divide * divide * x)%z # 결합
    
print(t *remain(a,b,c))

#GPT: 결합 단계에서 다시 계산하고 있기에 분할정복을 쓰는 이유중 하나인 (빠르게 계산)이 의미 없어짐