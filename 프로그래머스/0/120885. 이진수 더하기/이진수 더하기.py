def solution(bin1, bin2):
    add_list = list(map(int, str(int(bin1) + int(bin2))))

    for i in range(len(add_list) - 1, -1, -1):
        if add_list[i] >= 2:
            carry = add_list[i] // 2
            add_list[i] %= 2          
            
            if i > 0:
                add_list[i-1] += carry
            else:
                add_list.insert(0, carry)
                
    return "".join(map(str, add_list))
