class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,grade):
        self.grade=grade
        super().__init__(name,age)

Stu1=Student("Ajay",18,"A+")

print(Stu1.name,Stu1.age,Stu1.grade)

# Q2-
class Father:
    def skills(self):
        print("Art")

class Mother:
    def talents(self):
        print("Runner")

class Child(Father,Mother):
    pass

c=Child()
c.skills()
c.talents()

# Q3-
class Calculator:
    def add(self,a,b):
        return a+b
    
class Multiplier:
    def multiply(self,c,d):
        return c*d
    
class MathOperations(Calculator,Multiplier):
    pass

c1=MathOperations()
print(c1.add(89,67))
print(c1.multiply(65,45))