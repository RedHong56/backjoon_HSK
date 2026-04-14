import sys

times = int(sys.stdin.readline())

for _ in range(times):
    string = sys.stdin.readline().strip()
    print(string[0]+string[-1])