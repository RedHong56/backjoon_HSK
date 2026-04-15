import sys

string = sys.stdin.readline().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(string.find(i), end=' ')