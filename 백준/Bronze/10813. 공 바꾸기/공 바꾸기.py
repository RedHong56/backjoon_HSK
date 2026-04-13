import sys

basket_num, times = map(int,sys.stdin.readline().split())

basket = [i+1 for i in range(basket_num)]

for _ in range(times):
    idx_1, idx_2 = map(int, sys.stdin.readline().split())
    idx_1 -= 1
    idx_2 -= 1
    basket[idx_1] , basket[idx_2] = basket[idx_2], basket[idx_1]
    
print(" ".join(map(str,(basket))))