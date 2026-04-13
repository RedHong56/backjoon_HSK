import sys

basket_num, times = map(int,sys.stdin.readline().split())

basket = [0] * basket_num

for i in range(times):
    start, end, num = map(int,sys.stdin.readline().split())
    for j in range(start-1, end):
        basket[j] = num
print(" ".join(map(str,basket)))
