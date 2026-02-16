    # 2) Write a program to create class Student with following attributes: instance variables enrollment_no, name and branch; instance methods get_value() and print_value(); class variable cnt; static method show(). Variable cnt counts number of instances created and show() method displays value of cnt.

class Student:
        cnt = 0
        def __init__(self,enno='',  name='' , branch=''):
            self.enno  =enno 
            self.name = name 
            self.branch = branch 
            Student.cnt+=1

        def getValue(self):
            self.enno = input("enter enno: ") 
            self.name = input("enter name: ") 
            self.branch = input("enter branch: ") 
            (self.enno , self.name , self.branch) 

        def printValue(self):
            print(f"name:{self.name} \nenno:{self.enno}\nbranch:{self.branch}") 

        @staticmethod
        def show():
             print('total student created:', Student.cnt) 


s = Student() 
s.getValue() 
s.printValue()
s.show()


        