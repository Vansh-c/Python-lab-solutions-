# Create a program that will print out words that start with 's' from the below given statement.

s = input('enter text : ') 
list = s.split(" ") 
final_list = []

print(list)

for element in list:
    if(element.lower().startswith('s')):
        final_list.append(element)

print(" ".join(final_list))




