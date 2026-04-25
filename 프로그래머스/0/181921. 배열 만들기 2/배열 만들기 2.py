def solution(l, r):
    answer = []
    
    make_nums = ["5"]
    i = 0
    
    while i < len(make_nums):
        current = make_nums[i]
        
        if int(current) <= r:
            make_nums.append(current + "0")
            make_nums.append(current + "5")
            
        i += 1

    for num_str in make_nums:
        num = int(num_str)
        if l <= num <= r:
            answer.append(num)
            
    return answer if answer else [-1]