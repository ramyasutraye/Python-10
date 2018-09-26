t=float(input("enter your input:"))
t=t%(24*3600)
h=t//3600
t%=3600
m=t//60
t%=60
s=t
print("the output is:"h,m,s)
