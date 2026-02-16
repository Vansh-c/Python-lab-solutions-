
# Create and print a dictionary that contains keys a,b,c,d with their values 1,2,3 and 4 respectively using curly bracket syntax and ‘dict’ in built function.


print("==> using curly braces")
d = {
    'a':1 , 
    'b' : 2 ,
    'c' : 3 , 
    'd' : 4
}

print(d)

print('\n==> using inbuilt function') 

d = dict(a = int(1) , b = int(2) , c = int(3) , d = int(4))
print(d)