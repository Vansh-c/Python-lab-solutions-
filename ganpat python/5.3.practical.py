#Filter the dictionary by removing all items with a value greater than 2.


d= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(d) 

for key in list(d.keys()):
    if d[key] >2 :
        del d[key]

print(d)