l=int(input("Enter the lower limit for the range:"))
u=int(input("Enter the upper limit for the range:"))
if(l and u <=100000):
    for i in range(l,u+1):
        if(i%2==0):
            print(i)
else:
    print "invalid"
