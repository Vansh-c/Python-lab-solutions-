# Write a python program to check if a string is a palindrome or not


s1 = input('enter word: ') 
s2 = ""
k=0 
for i in range(len(s1)-1 , -1 , -1):
    s2 = s2+ s1[i] 
   

if(s2== s1):
    print('s1 and s2 are palindrome') 

else:
    print('not palindrome')

    
