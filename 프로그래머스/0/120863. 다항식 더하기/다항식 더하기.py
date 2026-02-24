def solution(polynomial):
    x_vari = 0
    const = 0
    
    for i in polynomial.split(" + "):
        if 'x' in i:
            if_x = i.replace('x', '')
            x_vari += int(if_x) if if_x else 1
        else:
            const += int(i)
            
    result = []
    if x_vari:
        result.append("x" if x_vari == 1 else f"{x_vari}x")
    if const:
        result.append(str(const))
        
    return " + ".join(result)