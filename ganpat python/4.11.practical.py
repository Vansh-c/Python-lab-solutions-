# Write a program to create a regular expression which verifies whether given mobile number is valid or not.

# s_input = input('enter phone number: ') 
# is_valid_number = True 

# if(len(s_input)!=10):
#     is_valid_number = False

# if s_input.isdigit() == False:
#     is_valid_number = False 

# if(is_valid_number):
#     print(f'{s_input} is a valid number') 

# else:
#     print('not a valid number')


import re


tocheck = re.compile(r'^[6,9]\d{9}$')
s_input = "9234535353"

if tocheck.match(s_input):
    print('valid number')
else:
    print('not a valid number')

