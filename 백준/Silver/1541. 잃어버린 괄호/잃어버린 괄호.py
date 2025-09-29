import re
a = re.split('([-+])', input())
result = []
result.append('(')
for i in a:
    if i == '-':
        result.append(')')
        result.append(i)        
        result.append('(')
    elif i == '+':
        result.append(i)
    else:
        result.append(int(i))

result.append(')')
# print(result)
s = (''.join(str(i) for i in result))

print(eval(s))

