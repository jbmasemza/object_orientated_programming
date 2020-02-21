class person:

    def __init__(self,name,age,gender,interest):
        self.name = name
        self.age = age
        self.gender = gender
        self.interest = ''.join(interest) 

    def hellow(self):
        return f'Hellow my name is {self.name} and I am {self.age}. My interest are {self.interest}'

person = person('Ryan',30,'male',['being a hardarse, ',' agile  and ', ' ssd hard drives '])
greeting = person.hellow()

print(greeting)

