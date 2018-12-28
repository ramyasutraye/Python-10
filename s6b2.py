numbers = [x for x in range(0, 10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
translate = dict(zip(numbers, numWords))
digits = {1:'only', 2: 'and', 3: 'hundred', 4: 'thousand'}
 
numDigits = 100
num = int(input())
res =""
 
#to loop till we get the answer
while numDigits >= 2:
   #to find number of digits
   
   numDigits = len(str(num))
 
   #to get the first digit
   numString = str(num)
   first = int(numString[0])
 
   #to get the first output and the thousand, hundred and 'and'
   if numDigits == 2:
      res += " " + digits[numDigits] + " " + translate[first]
   else:
      res += " " + translate[first] + " " + digits[numDigits]
   
   #to decrease by a digit we modulus divide by 1e(numDigits-1)
   num %= pow(10, numDigits-1)
print(res)
