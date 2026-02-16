# Write a program to find the sum of digit of an input number using while loop.

num = int(input("enter number : "))
sum = 0 

while(num!=0):
    r = num%10 
    sum = sum + r 
    num = int(num/10) 


print(sum)
