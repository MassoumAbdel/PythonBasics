# Functions execution file
# module, package, import
# ./src/functions/functions.py -> greet_user(),greet_user_by_name(),.....

from src.functions.functions import *
from src.functions.functions_return import *
# import line reads and executes the file
# you can use alias name for imported function - from src.functions.functions_return import greet_user() as greet
print(' ###### Execution: **********')
greet_user()
greet_user_by_name('john')
greet_user()
greet_user_by_name('jane')
greet_user()
greet_user_by_name('britney')
thank_you_by_name('abdel', 10)
thank_you_by_name('john', 7)
thank_you_by_name('jane', 5)
thank_you_by_name('britney', 20)

print('##### Execution of functions return **************')
print("Executing the functions with positional arguments")
print(get_full_name('john', 'doe'))
print(get_full_name('john', 'doe', 'brown')) # third argument is optional
# arguments you pass are positional, which will be assigned to each parameter based on position you enter
print(get_full_name('jane', 'doe', 'rogers'))
print(get_full_name('anne', 'doe'))

print("Executing the functions with keyword arguments (not positional arguments).")
print(get_full_name(first_name='momo', middle_name='kaka', last_name= 'switcher'))


print_all_names(['abdel', 'salah', 'mehdi'])


thank_you_by_name('Abdel',14)
cars = ['lexus', 'tesla', 'mercedise']
print_all_names(cars)




