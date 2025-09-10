'''정답이 여러 가지인 경우에는 아무거나 출력한다.'''
'''일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.'''
# import itertools # 경우의 수 

arr = list((int(input()))for _ in range(9))

total = sum(arr)

a = 0
b = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if total-100 == (arr[j]+arr[i]):
            a,b = j,i

            break
arr.pop(a)
arr.pop(b)
arr.sort()

for i in arr:
    print(i)

'''itertools.permutation'''

# for 2번