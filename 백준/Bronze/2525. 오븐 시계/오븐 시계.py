h, m = map(int,input().split())
time = int(input())

m += time

if m >= 60 :
    up = m//60
    h += up
    m -= up*60
    

if h > 23:
    h -= 24

print(h, m)