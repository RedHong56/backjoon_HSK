def solution(participant, completion):
    hash_dict = {}

    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1
        
    for c in completion:
        hash_dict[c] -= 1
        
    for key in hash_dict:
        if hash_dict[key] > 0:
            return key