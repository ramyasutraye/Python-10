n=int(input("enter N":))
a=[]
for i in range(1,n+1)
  s=input("strings:")
  a.append(s)
print(a)
b=zip(*a)
c=[x[0] for x in b if x==(x[0],)*len(x)]
print(c)
