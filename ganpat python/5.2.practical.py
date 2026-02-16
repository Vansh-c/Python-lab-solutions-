# Using above created dictionary perform following operations
# 1)Write a code to print out the value of a, d, and c.
# 2) Calculate the sum of the value of a,b,c,d and print it.
# 3)Add a new key, value pair (e,5) to the dictionary and print dictionary.


print("==> using curly braces")
d = {
    'a':1 , 
    'b' : 2 ,
    'c' : 3 , 
    'd' : 4
}

print(d)

print("==>printing value of a,d,c") 

for key in d:
    if(key != 'b'):
        print(d[key])

print('\n==>calculate sum of value of a,b,c,d and print it') 

sum = 0 

for key in d:
    sum += d[key]

print(f'sum = {sum}')

print("\n==>add  a new  key-value pair (e,5)") 

d['e'] = 5 
print(d)
    