import sys

subjects = int(sys.stdin.readline())

scores= list(map(int, sys.stdin.readline().split()))
max_score = max(scores)

new_scores = [s / max_score * 100 for s in scores]

avg = sum(new_scores) / subjects
print(avg)