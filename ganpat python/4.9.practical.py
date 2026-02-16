#Create a tuple with name courses and initialize it with JAVA, PHP, C#, Android. Insert two items HTML and Python at the 3rd position in tuple.

t = ('JAVA' , 'PHP' , "C#" , "Android") 
print(t)
t = list(t) 


t.insert(3 , 'HTML') 
t.insert(3, "PYTHON") 
print(tuple(t))

