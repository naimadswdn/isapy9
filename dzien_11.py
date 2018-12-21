class Animal(object):
    def __init__(self, legs_amount=4):
        self.legs_amount = legs_amount

    # def voice(self, voice='Grrr'):
    #     return f"{voice}"


class Master(object):
    def voice(self):
        print('Hello, I am a science Master!')


class Eng(object):
    def voice(self):
        print('Hello, I am a science Eng!')


class Man(Animal, Master, Eng):
    def __init__(self):
        super(Man, self).__init__()
        self.legs_amount = 2

    # def voice(self, voice='Hello'):
    #     return f"{voice}"


class Cat(Animal):
    pass


class Duck(Animal):
    def __init__(self):
        super(Duck, self).__init__()
        self.legs_amount = 2


class Dog(Animal):
    pass


class Student(Man):
    # def __init__(self):
    #     super(Man, self).__init__()
    pass


class Boxer(Dog):
    pass


class Dachshund(Dog):
    pass




# animal = Animal()
# print(f'Animal: {animal.voice()}')


man = Man()
print(f'Man: {man.voice()}')

student = Student()
print(f'Student: {student.voice()}')


duck = Duck()
cat = Cat()
boxer = Boxer()
dachshund = Dachshund()

# print(f'Man legs amount: {man.legs_amount}')
# print(f'Duck legs amount: {duck.legs_amount}')
# print(f'Boxer legs amount: {boxer.legs_amount}')
# print(f'Dachshund legs amount: {dachshund.legs_amount}')
# print(f'Cat legs amount: {cat.legs_amount}')
# print(f'Student legs amount: {student.legs_amount}')


