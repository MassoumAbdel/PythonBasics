# Chapter 9

def sample():
    pass


class Dog:
    # state
    bread = ''
    age = ''
    name = ''
    color = ''

    # behaviour
    # self keyword is used to show that functions and variable are belong to class
    def bark(self):
        print('Dog is barking')

    def run(self):
        print(f'{self.name} is running fast ....')

# creating the object from the class (model)
# creating the inctances from the class - INSTANTIATION
dog1 = Dog()
dog1.name = 'Roxi'

dog2 = Dog()
dog2.name = 'Flower'

dog3 = Dog()
dog3.name = 'Meli'

print('************  Behavior of dog: dogs are running ******')

dog1.run()
dog2.run()
dog3.run()








