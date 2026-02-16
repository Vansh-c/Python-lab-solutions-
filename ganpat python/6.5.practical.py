# Write a function to add two lists of the same length term-by-term & return new list 
# Eg.: A=listAdd([1,2,3],[1,2,3] )
# print (A) Will print [2,4,6].


def listAdd(l1 , l2):
    result  = []
    for i in range(len(l1)):
        result.append(l1[i] + l2[i])

    return result 


A = listAdd([1,2,3] , [3,4,5]) 
print(A)
