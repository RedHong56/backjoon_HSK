import sys

string = sys.stdin.readline().strip()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0

for char in string:
    for i in range(len(dial)):
        if char in dial[i]:
            result += (i + 3)

print(result)