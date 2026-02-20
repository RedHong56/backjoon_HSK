def solution(sides):
    longest = max(sides)
    if longest < sum(sides) - longest :
        return 1
    else:
        return 2