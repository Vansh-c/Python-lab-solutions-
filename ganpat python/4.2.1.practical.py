# Write a program to search an element, find maximum & minimum value from the list. 
# 1. Using inbuilt function 
# 2. Using for loop

# using inbuilt function 

l = [1,5,6,12,3,34,9] 
print(max(l)) 
print(min(l)) 
e = 5 
if e in l:
    print('element exist')
else:
    print('element do not exist') 


# without using inbuilt function 
max =  l[0] 
min = l[0] 
e = 3
exist = False
for i in range(len(l)):
    if(l[i]>max):
        max=  l[i] 

    if(l[i]<min):
        min = l[i] 

    if(l[i] == e):
        exist = True


print(f'max = {max} , min = {min} ,do element {e} exist = {exist}')



    


