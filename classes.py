class person:
    age = 32
    print(age)
p1 = person()
p2 = person()
p3 = person()
print(p1.age)




class student():
    Grade = 'A'
    print(Grade)
student1 = student()
student2 = student()
student3 = student()
student4 = student()
print(student1.Grade)
print(student2.Grade)
print(student3.Grade)
print(student4.Grade)

class Employees:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employees1 = Employees(name='John', age=56)
        Employees2 = Employees(name='Peter', age=34)
        Employees3 = Employees(name='Nick', age=45)
        print(Employees1)
        print(Employees2)
        print(Employees3)

class University():
    def __init__(self,name,location):
     self.name = name
     self.location ='Nairobi'
University1= University('Nairobi','San Francisco')
University2= University(name='JKWAT', location='Juja')
print(University)
print(University)

class student():
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks =marks
        print(self.name,self.age,self.marks)


    def display(self):
         print('Name ',self.name + ' and ' 'I am ',self.age,'years with marks', self.marks)

s1 = student(name='John',age=34,marks=356)
s2 = student(name='Peter',age=44,marks=456)
print(s1.display())
print(s2.display())


class parent():
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender =gender
        print(self.first_name,self.last_name,self.age,self.gender)

    def display(self):

            print(' My name is ',self.first_name,self.last_name, ' and ' ' i am ',self.age,' and am a ' ,self.gender)
p1 = parent('John','wind',age=34,gender='Male')
p2 = parent('Ann','wind',age=44,gender='Female')
p3 = parent('Mark','storm',age=34,gender='Male')
p4 = parent('Chris','jake',age=47,gender='Male')
print(p1.display())
print(p2.display())
print(p3.display())
print(p4.display())




