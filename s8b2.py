a=raw_input("")
l=len(a)
L=a.lower()
c=0
for i in range(0,l):
    if (a[i]=='a') or (a[i]=='e') or (a[i]=='i') or(a[i]=='o') or (a[i]=='u'):
        c=c+1
        break
if (c>0):
    print("Yes")
else:
    print("No")
