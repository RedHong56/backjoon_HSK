def solution(n, k):
    service = n//10
    beverage = (k - service) * 2000
    lamb = n * 12000
    return lamb + beverage