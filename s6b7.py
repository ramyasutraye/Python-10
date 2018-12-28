m=int(input(" "))
n=int(input(" "))
d=[]
for i in range(0,m):
    c=int(input(" "))
    d.append(c)
print(d.count(n))
if(d.count(n)==0):
    print("k is not here")
