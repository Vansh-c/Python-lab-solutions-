# Write a python program which shows the effect of mutability.

print("==> programming showing mutability") 
l = [1,2,3,4] 
l[0] = 88 
print(l)


print('\n==>Program showing immutabilty:') 
t= (1,2,3,4) 

try:
    t[1] = 90 
except:
    print('tuples cannot be modified ,they are immutable')