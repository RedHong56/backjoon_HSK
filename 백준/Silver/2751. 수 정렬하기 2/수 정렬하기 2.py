

'''입력 크기 확인

    최대 100만 개라서 input()만 쓰면 너무 느릴 수 있어.

    → sys.stdin.readline() 같은 빠른 입력 방식을 고려해야 해.

정렬 방법 선택

    파이썬 기본 sort()는 Timsort라서 O(N log N)이고 100만 개도 충분히 처리 가능해.

    직접 버블 정렬 같은 걸 쓰면 시간 초과 날 거야.

출력 최적화

    하나씩 print() 호출하면 느려.

    → "\n".join()으로 한 번에 출력하는 게 좋음.'''

import sys

rang = int(sys.stdin.readline())
list = list()
[list.append(int(sys.stdin.readline())) for _ in range(rang)]

list.sort()


for i in range(rang):
    print(list[i])
