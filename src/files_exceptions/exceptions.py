# chapter 10: Exception handling
import time

from src.o_o_programming.car_classes import *

car1 = car('toyota', 'highlander', 2023)

# try:
#     code to execute
# except CertainError as VariableToSaveAtTextError

try:
    car1.get_description()
    print(sum1) # triggers NameError
    print(f" new exception: {11 / 0}") # raises ZeroDivisionError
    print("car1.odometer_reading: ", car1.odmeter_reading)
    print("***** This line will not be seen if the previous line returns Error")
except AttributeError as error:
    print("Attribute ERROR was caught ....")
    print(f"body of the message: {error}")
except ZeroDivisionError as error:
    print(f"ERROR: can not divide by Zero: \t{error}")
except NameError as error:
    print(f"ERROR:  name error happened: {error}")
except TimeoutError as error:
    print("take a rest for 10 seconds...")
    time.sleep(10)

# you could put as much as except errors you got and describe them
# if you don't want them to display a system error

finally:
    print("This is the Finally block, executes regardless of any exception")

print('******************************')
print(car1.get_odometer())
car1.set_odometer(10000)  # testing the set_odometer
print(car1.get_odometer())