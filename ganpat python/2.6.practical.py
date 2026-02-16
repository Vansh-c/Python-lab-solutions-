# 6.	Write a python program for the library charges to fine for books returned late. Following are the fines: 
# First five days: 40 paisa per day.
# Six to ten day: 65 paisa per day. 
# Above ten days: 80 paisa per day

day = int(input('enter  the day for which the book was issued : ')) 
fine = 0 

if(day<=5):
    fine = 40 

elif (day>5 and day<=10):
    fine = 65 
elif(day>10):
    fine = 80 


print(f'the fine for {day} day is {fine}')




