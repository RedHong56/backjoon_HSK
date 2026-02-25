def solution(lines):
    count = 0
    
    graph = [0 for _ in range(200)]
    
    for line in lines:
        for i in range(line[0], line[1]):
            graph[i + 100] += 1
            

    for val in graph:
        if val >= 2:
            count += 1
            
    return count