n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The length is:",count)
if(n<0):
    print "invalid"
