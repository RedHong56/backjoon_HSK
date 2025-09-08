#1. 직사각형 크기
paper_X,paper_Y = map(int, input().split())
times = int(input())
cut_y = [0, paper_X] #가로축 리스트
cut_x = [0, paper_Y] #세로축 리스트

# #2. input 횟수 - x축으로 자르는지 or y축으로 자르는지
for _ in range(times):
    pos, cm = map(int, (input().split()))
    if pos == 0 :
        cut_x.append(cm)
    else:
        cut_y.append(cm)

# 종이 정렬하기
cut_x.sort()
cut_y.sort()

max_x = max( cut_x[i+1]-cut_x[i] for i in range(len(cut_x)-1) )
max_y = max( cut_y[i+1]-cut_y[i] for i in range(len(cut_y)-1) )
                                        
#. 곱하기
print(max_x*max_y)

