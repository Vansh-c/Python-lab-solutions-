# write  a user defined  function to sort a list

def sortList(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[j]> l[i]):
                t = l[i] 
                l[i] = l[j] 
                l[j] = t 

    return l


l = [4,1,3,2] 
print(sortList(l))

