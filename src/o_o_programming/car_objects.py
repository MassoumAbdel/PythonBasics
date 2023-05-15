# in this file we want to have a execution only (Objects)
from src.o_o_programming.car_classes import *

# created the object (instance of car class)
car1 = car('toyota', 'highlander', 2023)
car1.get_description()
print(f"car1.odometer_reading: {car1.odmeter_reading}")
print('----------------')
print(car1.get_odometer())
car1.set_odometer(10000)
print(car1.get_odometer())
car1.set_odometer = 5000 # does the same job as car1.set_odometer()
print(car1.get_odometer())
car1.set_odometer = 1000 # testing the logic here
print(car1.get_odometer())
car1.increment_odometer(50) # testing the increment_odometer
print(car1.get_odometer())
car1.increment_odometer(-50) # testing the increment_odometer
print(car1.get_odometer())
car1.increment_odometer('a')
print(car1.get_odometer())


# H/W: 9-4, 9-5












