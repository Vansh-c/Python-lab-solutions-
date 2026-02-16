# Write a python program to remove i’th character from string

st = "this is string" 
slist = list(st)
pos = 2 
k = 0 

for i in range(0 , len(slist)):
    if(i==pos):
        while(i+1<len(slist)):
            slist[i] = slist[i+1]
            i+=1

        slist.pop()   # removing last element
        

print(''.join(slist))
