import sys

#시간제한 2초

#가지고 있는 카드
n= int(sys.stdin.readline())
card = list(map(int ,sys.stdin.readline().split()))
# 주어진 카드
m= int(sys.stdin.readline())
deck = list(map(int ,sys.stdin.readline().split()))


#정렬된 카드 뭉치에서 골라서 찾기
card.sort()
ans = []
# 주어진 카드에 대해서 상근이가 있는 카드면 return 1 

#상근이의 카드를 하나 씩 찾기

for i in range(m):
    left = 0
    right = len(card)-1
    target = deck[i]

    while left <= right:
        
        mid = (left+right)//2 #뭉치의 인덱스 기준
        # 오른쪽에 있을때
        if target > card[mid]:
            left = mid + 1
        #왼쪽에 있을때
        elif target < card[mid]:
            right = mid -1
        #타겟을 찾았을때
        else:
                ans.append(1)
                break
            # print(f"true{card[i]}")

        if left>right:
            ans.append(0)
            break
        #타겟을 찾지 못했을때
        
        
print(" ".join(map(str, ans)))