# Write a Python program to filter a list of integers using lambda function. The program should filter even numbers from a given list.


l = [] 

for i in range(50):
    l.append(i) 

evenList = lambda i : [i for i in l if i%2==0]

print(evenList(l))