
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

# lab 1

class Mobile:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return print(f'mobile phone is {self.number} turned on')
        
    def turn_off(self):
        return print('mobile phone is turned off')

    def call(self, dest):
        return print(f'Calling {dest}')
    

jax = Mobile(number='+380671234567')
jax.turn_on()
jax.call('+380671234567')

# INSTANCE VARIABLES
class Demo:
    def __init__(self, value):
        self.instance_var = value

d1 = Demo(100)
d2 = Demo(200)

d1.var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)


class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter +=1
    def walk(self):
        pass
    def quack(self):
        print('quacks')

class Chicken:
    species = 'chicken'

    def walk(self):
        pass
    def cluck(self):
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('So many ducks were born:', Duck.counter)
for poultry in duckling, drake, hen, chicken:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()
        
#  Super class init

class Phone:
    counter = 0
    def __init__(self, number):
        self.number = number
        Phone.counter += 1
    def call(self, number):
        return f'Calling {number} using own number {self.number}'

class FixedPhone(Phone):
    last_SN = 0
    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = f'FP-{FixedPhone.last_SN}'

class MobilePhone(Phone):
    last_SN = 0
    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = f'MP-{MobilePhone.last_SN}'

print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)
print('Total number of mobile phones created:', MobilePhone.last_SN)

print(fphone.call('01632-960004'))
print(f'Fixed phone received "{fphone.SN}" serial number')
print(f'Mobile phone received "{mphone.SN}" serial number')

# LAB 2
import random

class Pack:
    counter = 0
    def __init__(self, number):
        self.number = number
        if self.number > 300:
            Pack.counter += 1

class Proce(Pack):
    first_Pack = 0
    def __init__(self, number):
        super().__init__(number)
        if self.number > 300:
            Proce.first_Pack += 1
            self.number -= 300
        self.PK = f'Number of pack: {Pack.counter}'
        
class Weight(Pack):
    def __init__(self, number):
        lower = 0.25
        upper = 0.5
        total = 0
        super().__init__(number)
        for _ in range(1, self.number+1):
            weight = random.uniform(lower, upper)
            total += weight 
        print(f'Total Weight is {total} grams')
        
        
apple = Proce(number=1000)
apple.__dir__()
apple.counter
apple.PK

random.uniform(.2, .5)

to = Weight(number=1000)
to.counter