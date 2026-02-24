def solution(my_string):
    num = 0
    temp =''
    
    for i in my_string:
        if i.isdecimal():
            temp += i
        else:
            if temp:
                num += int(temp)
                temp = ''
    if temp:
        num += int(temp)
    return num