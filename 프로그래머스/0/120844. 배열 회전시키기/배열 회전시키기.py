from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    if direction == 'right' :
        queue.appendleft(queue.pop())
    elif direction == 'left' :
        queue.append(queue.popleft())
        
    return list(queue)