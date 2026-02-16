# Write a program to create and initialize the tuple. Also remove 3rd element from tuple.

t = (1,2,3,4,5,6,7 ) 
t = t[:2] + t[3:]
print(t)