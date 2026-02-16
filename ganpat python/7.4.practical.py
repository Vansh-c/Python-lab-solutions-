# Write a Python program to write students information into csv file and read that details.

import csv 

with open('7.4.student.csv','a') as f:
    data = csv.writer(f) 
    s = input('write name , enno, py_marks: ') 
    s = s.split(',')
    data.writerow(s)

with open('7.4.student.csv','r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)

    