import datetime

class recruit:
    num_recruit = 0
    raise_amount = 1.04

    def __init__(self,first,last,age,race,pay):
        self.first = first
        self.last = last
        self.age = age
        self.race = race
        self.pay = pay
        self.email = first + '.' + last + '@umuzi.org'
        recruit.num_recruit += 1
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
     cls.raise_amount = amount

    @classmethod
    def from_string(cls, recruit_str):
        pass

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
           return False
        return True

class web_recruit(recruit):
    raise_amount = 1.01

    def __init__(self,first,last,age,race,pay,prg_lang):
        super().__init__(first,last,age,race,pay)
        self.prg_lang = prg_lang

class cohort_leader(recruit):
    raise_amount = 1.05

    def __init__(self,first,last,age,race,pay,cohorts = None):
        super().__init__(first,last,age,race,pay)
        if cohorts is None:
            self.cohorts = []
        else:
            self.cohorts = cohorts  

    def add_coh(self,coh):
        if coh not in self.cohorts :
            self.cohorts.append(coh)

    def remove_coh(self,coh):
        if coh in self.cohorts:
            self.cohorts.remove(coh) 

    def printt_coh(self):
        for coh in self.cohorts:
           print('-->',coh.fullname())  

    def __repr__(self):
        return "recruit('{}','{}','{}')".format(self.first,self.last,self.age,self.race,self.pay)

    def __str__(self):
        pass

 
        


web1 = web_recruit('palesa','lekoto',23,'black',6500,'python')
web2 = web_recruit('tebogo','sedibe',31,'black',6500,'java')

recruit1 = recruit('sophy','brown',19,'black',3500)
recruit2 = recruit('mike','adams',24,'white',3500)
recruit_str1 = 'john-lewis-19-indian-3500'
recruit_str2 = 'jane-lukhele-26-black-4500'
recruit_str3 = 'tshego-makena-22-black-5000'

first,last,age,race,pay = recruit_str1.split('-')
new_recruit1 = recruit(first,last,age,race,pay)

recruit.set_raise_amount(1.05)


my_date = datetime.date(2020,2,15)

cohortl_1 = cohort_leader('jane','smith',35,'white',15000,[web1])
cohortl_1.add_coh(web2) 
cohortl_1.remove_coh(web1) 

print(recruit1.email)
print(recruit2.email)
print(recruit1.fullname())
print(recruit1.pay)
recruit1.apply_raise()
print(recruit1.pay)
print(recruit.num_recruit)
print(recruit.raise_amount)
print(recruit1.raise_amount)
print(recruit2.raise_amount)
print(new_recruit1.fullname())
print(recruit.is_workday(my_date))
print(web1.email)
print(web1.prg_lang)
print(web1.pay)
web1.apply_raise()
print(web1.pay)
print(cohortl_1.email)
print(cohortl_1.printt_coh())
print(recruit1)
