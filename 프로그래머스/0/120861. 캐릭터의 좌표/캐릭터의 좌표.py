def solution(keyinput, board):
    x, y = 0, 0

    lim_x, lim_y = board[0] // 2, board[1] // 2
    
    key = {'up' : [0,1] , 'down' : [0,-1], 'left' : [-1,0], 'right' : [1,0]}
    
    for i in keyinput:
        dx, dy = key[i]
        if abs(x + dx) <= lim_x:
            x += dx
        if abs(y + dy) <= lim_y:
            y += dy
            
    return [x, y]