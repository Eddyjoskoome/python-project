# name = input("What is your name? ")
# weight = int(input("Please enter your weight in Kg..."))
# height = int(input("Please enter your height in M...."))
# BMI = (weight/height*2)
# print("Your BMI is " ,BMI, "Kg/m")
# if BMI <=0 and BMI>=18:
#     print("You are underweight")
# if BMI >=18 and BMI<=24:
#     print("You are normal")
# if BMI >=25 and BMI<=30:
#     print("You are overweight")
# if BMI >=31:
#     print("You need medical help")


#
# class staff:
#     def __init__(self,name,age,work,years):
#         self.name = name
#         self.age = age
#         self.work = work
#         self.years = years
# class teacher(staff):
#     def __init__(self,name,age,work,years,gender):
#         super().__init__(name, age, work, years)
#         self.gender = gender
#
# teacher1 = teacher("mark",30,"male",200,"male")
# print(teacher1.gender)

#
# class person:
#     def __init__(self,name,country,date_of_birth,gender):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
#         self.gender = gender
#     def display(self):
#         print('my name is ',self.name,'and my country is ',self.country,'i was born in ',self.date_of_birth,'and am a ',self.gender)
# person1 = person('Edddy','kenya',2005,'male')
# print(person1.display())
# age = input('Enter your date of birth ')
# print(age )
# year = 2024-int(age)
# print(year)

class person:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def get_person(self):
        return self
class employee:
    def __init__(self,age,salary):
        self.age = age
        self.salary = salary
class student:
    def __init__(self,gender,room,height):
        self.gender = gender
        self.room = room
        self.height = height

    @classmethod
class personalinfo(employee,student):
    def __init__(self,name,country,age,salary,gender,room,height,date_of_birth):
        super().__init__(name,country)

        self.date_of_birth = date_of_birth

personal1 = personalinfo('eddy',18,799900,9898888, 'male','opera' ,167,2005)
print(personal1.date_of_birth)










