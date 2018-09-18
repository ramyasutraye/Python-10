x = []
n=int(input("how many numbers:"))
for i in range(1,n+1):
    b=int(input("numbers:"))
    x.append(b)
x.sort()
print"the median of x is:",sorted(x)[len(x)//2]
