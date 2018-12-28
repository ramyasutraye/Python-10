n = int(input("Please Enter any Number: "))
Count = 0
while(n > 0):
    n = n // 10
    Count = Count + 1
print("\n%d" %Count)
