def solution(a, b, c, d):
    dice = [a, b, c, d]
    unique = list(set(dice)) 
    
    if len(unique) == 1:
        return 1111 * unique[0]
        
    elif len(unique) == 2:
        num1, num2 = unique

        if dice.count(num1) == 3:
            p, q = num1, num2
            return (10 * p + q) ** 2

        elif dice.count(num2) == 3:
            p, q = num2, num1
            return (10 * p + q) ** 2

        else:
            p, q = num1, num2
            return (p + q) * abs(p - q)

    elif len(unique) == 3:
        qr = []
        
        for num in unique:
            if dice.count(num) == 2:
                p = num
            else:
                qr.append(num)
        return qr[0] * qr[1]
    
    else:
        return min(dice)