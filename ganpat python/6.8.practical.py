# Write a Python program to sort a list of dictionaries using lambda function. The program should sort the list based on the 'age' key in each dictionary

print("power levels of dbz anime characters are:")
dic = [
   {'name':"krillin" , 'powerlvl':45000} , 
   {'name':'goku',  'powerlvl':150000000} , 
   {'name':'frieza' , 'powerlvl':120000000}
]

sortedDict = sorted(dic, key =lambda x:x['powerlvl'] , reverse= True)  

print(sortedDict)