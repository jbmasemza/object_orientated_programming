class person:

    def __init__(self,name,age,interest):
        self.name = name
        self.age = age
        self.interest = ''.join(interest) 

    def hellow(self):
        return f'Hellow my name is {self.name} and I am {self.age}. My interest are {self.interest}'

person = person('Ryan',30,['being a hardarse ',' agile ', ' ssd hard drives '])
greeting = person.hellow()

print(greeting)

