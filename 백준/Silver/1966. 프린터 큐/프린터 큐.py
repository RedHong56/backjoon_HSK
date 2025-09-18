'''나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
https://www.acmicpc.net/problem/1966'''
import sys
from collections import deque
tc = int(sys.stdin.readline()) # tc 수


for _ in range(tc):
    

    n , m = map(int,sys.stdin.readline().split()) # 문서의 총 갯수, 알고싶은 문서
    core = list(map(int,sys.stdin.readline().split())) #문서의 중요성
    paper = deque()
    for i in range(n): #deque에 삽입
        paper.append((core[i],i))
    core.sort()
    count = 0
    
    while True:     
        cou = paper[0]
        if cou[0]==core[-1]:
            count += 1
            a=paper.popleft()
            core.pop()

            if cou[1] == m:
                print(count)
                break
        else: 
            paper.append(paper.popleft())
            # print(paper)