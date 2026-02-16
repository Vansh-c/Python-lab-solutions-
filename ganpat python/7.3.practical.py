# Write a Python program to read first n lines of a file.

f = open('practical 7\\7.3.test.txt' , 'r')

for i in range(5):
    data = f.readline() 
    print(data)

