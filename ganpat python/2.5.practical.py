# 5.	Write a python program to check if a given character is a vowel or not.


c = input('enter character : ') 

if(len(c)==1):
    if(c=='a' or c=='e' or c=='i' or c=='e' or c=='u'):
       print('enter character is vowel') 

    else:
       print('entered character is  consonant')

else:
   print('enter character length should be strictly 1')