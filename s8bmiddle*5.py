n=raw_input(" ")
if(len(n)%2==0):
    n=n[:int((len(n)/2))-1]+'**'+n[int(len(n)/2)+1:]
else:
    n=n[:int(len(n)/2)]+'*'+n[int(len(n)/2)+1:]
print(n)
