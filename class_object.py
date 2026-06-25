class Rectangle:
        def __init__(self,length,width):
            self.length=length
            self.width=width

        def area(self):
            area=self.length*self.width
            return area

        def perimeter(self):
            perimeter=2*(self.length+self.width)
            return perimeter

a=int(input("Enter length of rectangle :"))
b=int(input("Enter width of rectangle :"))

r=Rectangle(a,b)

print("Area:",r.area())
print("Perimeter:",r.perimeter())

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Student name : {self.name}")
        print(f"Student marks : {self.marks}")

s1=Student("Ashish",77)
s2=Student("Swayam",97)

s1.display()
print()
s2.display()