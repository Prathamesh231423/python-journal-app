class Student:       #class is a keyword used to create blueprint of an objects
    def __init__(self,name,age,marks):
        self.name=name  #self refers to current object
        self.age=age
        self.marks=marks

    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Marks:",self.marks)

s1=Student("Akash Deep", 15 , 88)   #s1 and s2 are objects of the class
s2=Student("Shivam", 16 , 78)

s1.display()
print()
s2.display()


    


    