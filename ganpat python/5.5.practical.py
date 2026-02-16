# You have 4 films in the dictionary with the age and number of seats available as indicated below. Write a programme to ask for a film and check for the person that he is eligible to watch movie, also check ticket availability and movie availability in the cinema.


d = {
           "War": [3,5],
        "Bourne": [18,5],
        "Gully boy": [15,5],
        "Uri":[12, 5]
}

ask  = input("enter name of movie: ") 
age = int(input("enter your name: ")) 

if ask in d :
    if(age> d[ask][0] and d[ask][1]>0):

       print('yes')
       print(f'movie name = {ask}')
       print(f"ticket availaible = {d[ask][1]}")
       d[ask][1] = d[ask][1] - 1 
       print(f"movie:{ask}  , tickets left = {d[ask][1]}")

# print(d)
