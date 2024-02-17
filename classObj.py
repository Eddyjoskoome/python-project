class employees:
    raise_amount = 1.04
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + ('@gmail.com')
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
class developer(employees):
    def __init__(self,first_name,last_name,pay,language):
        super().__init__(first_name,last_name,pay)
        self.lang = language
class professor(employees):
    def __init__(self,first_name,last_name,pay,gender):
        super().__init__(first_name,last_name,pay)
        self.gender =gender

emp1=employees("eddy",'jos',3000000,)
emp2=employees("jayne",'waithira',6000000)
print(emp1.first_name)
print(emp2.first_name)
print(emp1.email)
print(emp2.email)
print(f"{emp1.first_name} {emp1.last_name} salary is {emp1.pay}")
print(f"{emp2.first_name} {emp2.last_name} salary is {emp2.pay}")
print(emp1.full_name())
print(emp2.full_name())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)
employees.raise_amount = 4.56
print(employees.raise_amount)
print(emp1.pay)
print(emp2.pay)
dev1=developer("john","doe",600000,'phython')
dev2=developer("anna","john",600000,'HTML')
print(dev1.lang)
print(dev2.lang)

3