a=[]
n=int(input("N:"))
for i in range(0,n):
    b=int(input("Numbers:"))
    a.append(b)
print(a)
c=[]
for x in range(n):
    if(a.count(a[x])>1):
            c.append(a[x])
print set(c)
if len(c)!=0:  
    print "not unique"  
else:  
    print "unique"  
    
