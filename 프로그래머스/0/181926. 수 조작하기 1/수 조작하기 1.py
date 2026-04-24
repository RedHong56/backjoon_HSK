def solution(n, control):
    
    cmd = {"w": 1, "s": -1, "d": 10, "a": -10}
    
    for c in control:
        n += cmd[c]
        
    return n