h, m = map(int, input().split())

convert_h =h*60
if h == 0 and m < 45:
    x = 23
    y = 60+m - 45
else:
    x= (convert_h+m-45) //60
    y= (convert_h+m-45) %60

print(f"{x} {y}")