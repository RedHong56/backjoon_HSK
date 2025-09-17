import sys
import heapq

n = int(sys.stdin.readline())

hq = []
count = 0
for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0 :
        print(-heapq.heappop(hq) if hq else 0)
    else: heapq.heappush(hq, -m)
