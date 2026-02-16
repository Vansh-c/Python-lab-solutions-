# 1) Create a class Employee with data members: name, department and salary. Use constructor to initialize values and display() method for printing information of three employees

class ShowDetails:
    def __init__(self, name , department , salary):
        self.name = name  
        self.department = department 
        self.salary = salary 

    def display(self):
        print(f"name = {self.name}\ndepartment = {self.department}\nsalary = {self.salary}") 


a = ShowDetails('Vansh Joshi' , "IT" , "10000000") 
a.display()