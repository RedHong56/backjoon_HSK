import sys
import heapq

n = int(sys.stdin.readline())
hq = []
lq = []
for i in range(n):
    a=int(sys.stdin.readline())
    if not hq or a <= -hq[0]:
        heapq.heappush(hq, -a)
    else:
        heapq.heappush(lq, a)

    if len(hq)>len(lq)+1:
        heapq.heappush(lq, -heapq.heappop(hq))
    elif len(lq)>len(hq):
        heapq.heappush(hq, -heapq.heappop(lq))


    if lq and -hq[0] > lq[0]:
        l = -heapq.heappop(hq)
        r = heapq.heappop(lq)
        heapq.heappush(hq, -r)
        heapq.heappush(lq, l)
    print(-hq[0])