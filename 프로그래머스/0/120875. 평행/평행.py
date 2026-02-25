def solution(dots):

    pairs = [[(0,1), (2,3)], [(0,2), (1,3)], [(0,3), (1,2)]]
    
    for p1, p2 in pairs:

        slope1 = (dots[p1[0]][1] - dots[p1[1]][1]) / (dots[p1[0]][0] - dots[p1[1]][0])
        slope2 = (dots[p2[0]][1] - dots[p2[1]][1]) / (dots[p2[0]][0] - dots[p2[1]][0])
        
        if slope1 == slope2:
            return 1
            
    return 0