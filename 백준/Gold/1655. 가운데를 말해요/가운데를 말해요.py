import sys
import heapq

n = int(sys.stdin.readline())
hq = []
lq = []



for i in range(n):
    a=int(sys.stdin.readline())
    
    #처음에 수를 분배하기
    if not hq or a <= -hq[0]:
        heapq.heappush(hq, -a)
    else:
        heapq.heappush(lq, a)

    #서로 계속 섞어주는 과정 길이가 다르면
    if len(hq)>len(lq)+1:
        heapq.heappush(lq, -heapq.heappop(hq))
    elif len(lq)>len(hq):
        heapq.heappush(hq, -heapq.heappop(lq))

    #팝하여 옮겨주기
    if lq and -hq[0] > lq[0]:
        l = -heapq.heappop(hq)
        r = heapq.heappop(lq)
        heapq.heappush(hq, -r)
        heapq.heappush(lq, l)
    print(-hq[0])