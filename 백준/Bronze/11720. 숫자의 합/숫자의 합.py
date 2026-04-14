import sys

times = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

sum_num = 0

for i in range(times):
    sum_num += int(string[i])

print(sum_num)