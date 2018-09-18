x = []
n=int(input("how many numbers:"))
for i in range(1,n+1):
    b = int(input("numbers:"))
    x.append(b)
for index,y in enumerate(x):
    print index,y
