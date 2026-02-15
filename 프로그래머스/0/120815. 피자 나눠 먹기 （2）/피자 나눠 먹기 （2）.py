def solution(n):
    answer = 0
    a, b = n, 6
    
    while b:
        a, b = b, a % b
    gcd = a
    
    lcm = (n*6) // gcd
    
    answer = lcm // 6
    
    return answer