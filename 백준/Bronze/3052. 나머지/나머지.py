cnt = set()

for _ in range(10):
    num = int(input()) % 42
    
    cnt.add(num)

print(len(cnt))