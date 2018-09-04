N = int(input("Enter a number: "))    
if N < 0:  
   print("invalid number")  
else:  
   sum = 0   
   while(N > 0):  
       sum += N  
       N -= 1  
   print("The sum of given natural number is:",sum)  
