# Chapter 9

def sample():
    pass


class Dog:
    # state/attributes
    # execute automatically by python when class is instantiated (when object is created)
    bread = ''
    age = ''
    name = ''
    color = ''

    def __init__(self, name1, breed1, age1, color1):
        self.name= name1
        self.bread = breed1
        self.age = age1
        self.color = color1

    # behaviour
    # self keyword is used to show that functions and variable are belong to class
    def bark(self):
       # print('Dog is barking')

    def run(self):
        abc= self.name
        print(f'{self.name} is running fast ....')
        # print(f'{self.name} is running fast ....')
        self.bark()

# creating the object from the class (model)
# creating the instances from the class - INSTANTIATION
dog1 = Dog('Roxi', 'Husky', 3, 'back/white')
# dog1.

# dog1 = Dog()
# dog1.name = 'Roxi'
# dog1.breed = 'Husky'
# dog1.age = 3
# dog1.color = 'black/white'


dog1 = Dog('Flower', 'Husky', 3, 'back/white')
dog2.name = 'Flower'

dog3 = Dog()
dog3.name = 'Meli'

print('************  Behavior of dog: dogs are running ******')

dog1.run()
dog2.run()
dog3.run()


# H/W: 9-1, 9-2, 9-3,





