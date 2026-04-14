import sys

basket_num, times = map(int, sys.stdin.readline().split())

basket = [i+1 for i in range(basket_num)]

for _ in range(times):
    i, j = map(int,sys.stdin.readline().split())
    basket[i-1:j] = basket[i-1:j][::-1]

print(" ".join(map(str, basket)))