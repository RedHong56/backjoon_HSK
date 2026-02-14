def solution(numer1, denom1, numer2, denom2):
    add_denom = denom1 * denom2 #분모
    add_num = numer1 * denom2 + numer2 * denom1 #분자

    # 분자와 분모 비교
    
    # 최대 공약수
    a, b = add_num, add_denom
    
    while b:
        a, b = b, a % b
    answer = [add_num // a, add_denom // a] 
    
    return answer