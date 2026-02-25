def solution(score):
    answer = []

    sums = [s[0] + s[1] for s in score]

    rank_ref = sorted(sums, reverse=True)
    
    for s in sums:
        answer.append(rank_ref.index(s) + 1)
            
    return answer