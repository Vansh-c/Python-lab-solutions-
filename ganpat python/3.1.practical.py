# Write a program to check if number is Armstrong

number = int (input("enter num: "))
orig_no =  number 
compareNumber = number
n = 0 

while(number!=0):
    n = n+1
    number = int(number/10)

new_number = 0 

while(orig_no!=0):
    r = orig_no%10
    r = r**n

    new_number = new_number + r
    orig_no = int(orig_no/10)


if(compareNumber == new_number):
    print(f'{new_number } is armstrong') 

else:
    print(f'{new_number} is not armstrong')





