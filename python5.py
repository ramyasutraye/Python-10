print("enter three numbers:")
 
l = int(input())
m = int(input())
n = int(input())
if l>m and l>n:
    print(l, " is largest")
elif m>l and m>n:
    print(m, " is largest")
else:
    print(n, " is largest")

