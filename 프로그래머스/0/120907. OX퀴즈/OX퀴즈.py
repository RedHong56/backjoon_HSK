def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split(' ')
        
        num1 = int(parts[0])
        op = parts[1]
        num2 = int(parts[2])
        result = int(parts[4])

        if op == '+':
            calculator = num1 + num2
        else:
            calculator = num1 - num2
            
        if calculator == result:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer