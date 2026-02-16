# 7.	Write a python program to count odd numbers from given three numbers and display maximum odd number.
a = int(input("enter a: ")) 
b = int(input('enter b: '))
c = int(input('enter c: '))

store_odd = [] 

if(a%2==1):
    store_odd.append(a) 

if(b%2==1):
    store_odd.append(b) 

if(c%2==1):
    store_odd.append(c)

max_odd=  0 

for i in range(len(store_odd)):
    if(store_odd[i] > max_odd):
        max_odd = store_odd[i] 


print(f'maximum odd number is {max_odd}')
     

