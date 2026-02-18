def solution(hp):
    answer = 0
    
    major = hp // 5
    hp -= major * 5
    
    soldier = hp // 3
    hp -= soldier * 3
    
    worker = hp // 1
    hp -= worker * 1
    
    return major + soldier + worker