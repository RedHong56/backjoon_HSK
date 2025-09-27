import sys
sys.setrecursionlimit(100_000)

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()

DP = [[-1]*(len(m)+1) for _ in range(len(n)+1)]

def sequence(i,j):
    if i<=0 or j<=0:
        return 0
    if DP[i][j] != -1: # 바뀌면 다시 그대로 반환해줘잉~~
        return DP[i][j]
    
    if n[i-1] == m[j-1]:
        DP[i][j] = sequence(i-1,j-1) + 1
    else:
        DP[i][j] = max(sequence(i,j-1), sequence(i-1,j))
    return DP[i][j]

print(sequence(len(n), len(m)))
