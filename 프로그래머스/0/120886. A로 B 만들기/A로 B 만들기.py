def solution(before, after):
    pre = sorted(before)
    post = sorted(after, reverse=True)
    
    for i in pre:
        j = post.pop()
        if i != j:
            return 0
    
    return 1