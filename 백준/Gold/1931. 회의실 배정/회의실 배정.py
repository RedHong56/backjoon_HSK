import sys
n = int(sys.stdin.readline())
count = 0
arr = []
for _ in range(n):
    a, b =map(int,sys.stdin.readline().split())
    c= b-a
    arr.append([a,b,c])
arr.sort(key = lambda x: (x[1], x[0]))
# print(arr)
# print("----------------------")
end = 0
for a,b,c in arr:
    if end <= a:
        end = b
        count+=1
        # print(end)
print(count)