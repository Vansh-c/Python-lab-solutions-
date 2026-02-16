# Write a Python program to combine each line from first file with the corresponding line in second file.

f1= open('practical 7\\test1.txt','r') 
# print(f1.read()) 
f2 = open('practical 7\\test2.txt','r') 
# print(f2.read())

finaldata = f1.read() + f2.read() 

f3 = open("practical 7\\final.txt", 'w')
f3.write(finaldata)
print('wrote succesfully in a file .')
