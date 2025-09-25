n = int(input())

def fivonacci(a):
    arr = [0] * (a+1)
    arr[0] = 0
    arr[1] = 1
    i = 2
    while arr[a] == 0:
        arr[i]= arr[i-1]+arr[i-2]
        i += 1

    return arr[a]



print(fivonacci(n))