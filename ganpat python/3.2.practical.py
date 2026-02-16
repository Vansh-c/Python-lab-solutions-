# Write a program to check special number. (Number is equal to the sum of its divisors)

n = 28 
sum = 0 
storenum = n 

for i in range(1,n):
    if(n%i==0):
        sum = sum + i 

if(storenum == sum):
    print(f'{sum} is a perfect number') 

else:
    print(f'{sum} is  not a perfect number')