# Write a function to find the minimum and maximum value from argument list & return both minimum & maximum in tuple form. 
#  arg is  a tuple  which contains all arguments. 

def findMinMax(*numbers):
    max  = numbers[0] 
    
    for  i in numbers:
        if(i>max):
            max = i 

    min = numbers[0] 

    for i in numbers:
        if(i<min):
            min = i 

    return (max , min) 


print(findMinMax(4,3,-1,2,8,3))
