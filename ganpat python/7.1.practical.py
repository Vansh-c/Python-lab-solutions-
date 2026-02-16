# Write a Python program to read content from a file and display the word with maximum length. 

f = open('test.txt' , 'r')

data = f.read()


count = 0 
maxlen = 0 

for i in data:
    if(i==' ' or i.isalnum()==False):
        count = 0 

    if(count>maxlen):
        maxlen = count

    count+=1 

print(data)
print('maxlen = '  , maxlen)
