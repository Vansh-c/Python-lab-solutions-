# Write a program to display all the prime numbers between 1 to n using function.

def displayPrimeNumbers(n):
    
   for i in range(2,n):
      isprime = True 
      for j in range(2,i):
          if(i%j==0):
              isprime= False 
              break
      
      if(isprime== True):
        print(i)


displayPrimeNumbers(200)