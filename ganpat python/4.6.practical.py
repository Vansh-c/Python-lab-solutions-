# Write a Python program which takes a list and returns a list with the elements "Shifted left by one position" so [1, 2, 3] yields [2, 3, 1].
# Example: [11, 12, 13] → [12, 13, 11]

l = [1,2,3] 
zeroth_element = l[0]

for i in range(len(l)-1):
    l[i] = l[i+1] 

l[len(l)-1] = zeroth_element

print(l)
