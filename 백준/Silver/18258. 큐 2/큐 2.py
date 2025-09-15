import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque() #deque 사용
out = []

for _ in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        queue.append(a[1])
    elif a[0] =="front":
        out.append(queue[0]if queue else -1)
    elif a[0] =="back":
        out.append(queue[-1] if queue else -1)
    elif a[0] =="size":
        out.append(len(queue))
    elif a[0] =="empty":
        out.append(0 if queue else 1)
    elif a[0] =="pop":
        out.append(queue.popleft() if queue else -1)

sys.stdout.write("\n".join(map(str, out)))

#print() 오버헤드, 버퍼 flush
'''print()의 특징

내부적으로 문자열 변환(str()), 공백/줄바꿈 처리(end, sep), 버퍼 flush 여부를 매번 확인합니다.
작업이 누적되어 시간 초과를 유발할 수 있습니다.

2. sys.stdout.write()의 특징
단순히 문자열을 그대로 표준 출력 버퍼에 넣는 함수.
자동 개행이 없어서 "\n"을 직접 붙여야 함.
문자열을 한 번에 join 해서 몰아서 출력하면 I/O 호출이 최소화됩니다.

3. 왜 sys.stdout.write()를 쓰는가?

백준 / 프로그래머스 / 코드포스 같은 곳에서 입력·출력 데이터가 수십만 줄일 때, print()보다 훨씬 빠릅니다.
특히 큐, 스택 문제처럼 출력이 많을 때 시간 초과 방지용 표준 패턴.
'''