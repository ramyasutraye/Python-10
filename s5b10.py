n=int(input(" "))
for i in range(2,100):
    if(2**i==n):
        print(2,"^",i)
    else:
        print("not power of two")
