# 1~ N 까지 있음
# k 주어지면 k번째 사람 제거 이걸 요세푸스 순열이라고 한다
from collections import deque
import sys
n, k = map(int,sys.stdin.readline().split())

q = deque(range(1,n+1))
ans = []
while len(q) > 0 :
    for _ in range(k-1):
        q.append(q[0])
        q.popleft()
    ans.append(q[0])
    q.popleft()

print(f"<{', '.join(map(str, ans))}>")


# join → 리스트 원소들을 문자열로 합쳐 하나의 문자열 만듦.

# sys.stdout.write → 문자열을 화면에 바로 써줌 (자동 줄바꿈 없음, 문자열만 가능).
