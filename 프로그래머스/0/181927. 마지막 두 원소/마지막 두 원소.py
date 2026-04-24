def solution(num_list):
    pre_last = num_list[-2]
    last = num_list[-1]
    
    if last > pre_last:
        num_list.append(last-pre_last)
    else:
        num_list.append(2*last)
    
    return num_list