# Write a program to count number of digits, upper-case characters and lower-case characters from the string.
import string 

st = "this  is a String890" 

countlower = 0 
countupper = 0 
countdigit  = 0 

for i in range (0 , len(st)):
    if(st[i].isupper()):
              countupper+=1 

    if(st[i].islower()):
           countlower+=1

    if(st[i].isdigit()):
           countdigit+=1 


print(f"lowercase = {countlower}, uppercase = {countupper} , digits = {countdigit}")