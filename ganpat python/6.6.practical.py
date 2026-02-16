# WAP a function called powers(n) that prints out the first 5 powers of a given number. 
# Eg. >>> powers(6) 
# The first 5 powers of 6 are: 1 6 36 216 1296

def powers(n):
    print(f"first 5 power of {n} = ", end=' ')
    for i in range(5):
        print(n**i, end=' ') 


powers(6)