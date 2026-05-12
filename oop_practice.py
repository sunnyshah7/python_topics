# Classes, inheritance, polymorphism, encapsulation

class Car():
    def show(self):
        print("This is car function")


C = Car()
# C.show()g

# Remark : self is required because it refers to the current obj

#  use of instance variable.

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def student_details(self):
        print(f"{self.name}'s + age is {self.age}")
    

stu = Student("sunny",25)

# stu.student_details()


# use of  class variable 

class Employee():
    company = "Infosys"
    
    def show(self):
        print(f" The company in which i work is {self.company}")
E = Employee()

# E.show()


# constructor in python

# there are 2 types of constructor in python

# 1. default constructor

class Student:
    def __init__(self):
        print("this is defalut contstructor is called")

# stu = Student()

# Note: so whenever we create a  obj onf a class the default constructor automatically gets called.


# 2. parameterized constructor

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def show(self):
        print(f"{self.name}'s age is {self.age}")

# stu = Student("sunny",26)

# stu.show()


# Inheritance in python and its type


# i.) single inheritance 

class Animal:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    

class Dog(Animal):
    def show(self):
        print(f"The name of the dog is {self.name} and its breed is {self.breed} ")

D = Dog("dubby", "labrador")
D.show()

# ii.) Multilevel Inheritance

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

# 3. Multiple Inheritance
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()
c.skill2()

# 4. Hierarchical Inheritance

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass



# use of super class

class School:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(School):
    def __init__(self,name,age,city):
            self.city = city
            super().__init__(name,age)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.city)
        

Stu = Student("sunny",12,"raxaul")
Stu.display()