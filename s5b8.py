n=int(input(" "))
c=0
if(n>0):
        for i in range(0,n):
                c=int(input(" "))
                c=c+c
        print(c/n)
else:
        print("invalid")
