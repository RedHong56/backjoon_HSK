import sys
n = int(sys.stdin.readline())

#f(n) = f(n-1)+f(n-2) 단, n이 2보다 클때

mod = 15746


def dongju_saekki(r):
    if r == 1:
        return print(1)
    if r == 2:
        return print(2)

    a,b = 1,2

    for i in range(3, n+1):
        #(n-1) (n-2)
        a,b =b ,(a+b)%mod
    return print(b)

dongju_saekki(n)
#출력 길이가 n인 모든 2진 수열 개수를 15746으로  나눈 나머지

