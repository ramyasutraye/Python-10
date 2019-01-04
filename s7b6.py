a=int(input(" "))
flag=0
for i in range(2,a):
    if(a%i==0):
        flag=flag+1

if(flag==0):
    print("prime")
else:
    print("not prime")
