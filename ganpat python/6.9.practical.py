# Write a Python program to execute a function on each element of a list using lambda function. The program should calculate square of all numbers.


l  = [1,2,3,4,5,6,7,8,9,20] 

squareList= lambda n:[i**2 for i in l] 

print(squareList(l))