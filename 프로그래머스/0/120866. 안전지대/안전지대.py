def solution(board):
    n = len(board)
    count = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: 
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                            board[nx][ny] = 2

    for row in board:
        count += row.count(0)
    return count