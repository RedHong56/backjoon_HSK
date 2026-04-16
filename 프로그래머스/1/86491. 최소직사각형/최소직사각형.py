def solution(sizes):
    w, h = 0, 0
    for card in sizes:
        card_w = max(card)
        card_h = min(card)
        
        if w < card_w:
            w = card_w
        if h < card_h:
            h = card_h
        
    
    answer = w*h
    return answer