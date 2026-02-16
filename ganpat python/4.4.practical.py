# WAP to sort element in list 
# 1. In same list 
# 2. Create sorted copy of original list & print both.
# 3. Sort without any built-in function

print("==> sorting the list")
l = [3,4,1,5,2] 
l.sort() 
print(l)

print("\n==>creating copy sorting the copied list and printing both of them:") 
l = [6,4,1,9,0] 
m = l 
m.sort() 
print(l) 
print(m)


print("\n==>sorting by using function") 

l = [12,33,2,78,9] 

for i in range(len(l)):
    for j in range(i+1 , len(l)):
        if(l[j] < l[i]):
            l[j] , l[i] = l[i] , l[j]

print(l)


