class colour:
    def __init__(self, number, type, position):
        self.number = number
        self.type = type
        self.position = position

class question(colour):
    def __init__(self, number, type,position,area):
        super().__init__(number, type, position)
        self.area = area
class answer(colour):
    def __init__(self, number, type,position,length):
        super().__init__(number, type, position)
        self.length = length
question1 = question(56,"blue",'right','center')
answer1 = answer(56,"blue",'left','long')
print(question1)
print(answer1)