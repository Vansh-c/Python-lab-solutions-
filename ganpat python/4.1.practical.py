


# 🔹 Difference between insert, append, and extend
# Operation	      What it does	                                       Syntax	Example
# insert()	      Adds one element at a specific index	               list.insert(index, item)	l.insert(1, "CS")
# append()	      Adds one element at the end	list.append(item)	   l.append(90)
# extend()	      Adds multiple elements to the end	                   list.extend(iterable)	l.extend([1,2,3])


anime = ['ichigo' , "byakuya kuchiki" , "kenpachi zaraki"] 
print(anime) 
print()

print('==> after appending') 
anime.append("grimjoww") 
print(anime)
print() 

print('==> after inserting') 
anime.insert(2, "shunsui kyorakiu") 
print(anime) 
print() 

print('==> after extending') 
anime.extend(["jushiro Ukitake" , "Retsu Unohana" , "Renji Abarai"]) 
print(anime)