# Multi Level Inheritance
class Student:
    start_time="10 am"
    end_time="6pm"

class AdminStaff(Student):
    def __init__(self,role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary

acc=Accountant(25000,"CA")
print(acc.role,acc.salary,acc.start_time,acc.end_time)

# Multiple Inheritance
class Teacher:
    def __init__(self,salary):
        self.salary=salary

class Student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name=name

ta1=TA(15_000,9.3,"Prathamesh")
print(ta1.name,ta1.gpa,ta1.salary)




