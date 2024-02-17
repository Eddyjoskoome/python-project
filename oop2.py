# class Magari:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def onyesha(self):
#         print(f'My favourite car is {self.name}')
#
# myobj = Magari('Toyota',2000000000)


#creat a class called fruit should have name price and colour...reat a method like statment tuh
#creat an  5 object....

class fruit:
    def __init__(self,name,price,colour):
         self.name = name
         self.price = price
         self.colour = colour

    def display(self):
        print('My favorite fruit is ', self.name , 'it costs', self.price , 'and it has a bright',  self.colour)

f1 = fruit('Apple',30,'green ones')
f2 = fruit('Pear',40,'green ones')
f3 = fruit('Strawberry',60,'red ones')
print(f1.display())
print(f2.display())
print(f3.display())