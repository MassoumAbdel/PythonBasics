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
# car1.increment_odometer('a')
# print(car1.get_odometer())

print('********* Creating the electric car object ...')
tesla1 = ElectricCar('tesla', 'X', 2023)
# after adding battery size to __init__, we can still use 3 argument
# because battery_size was added as optional parameter

tesla1.get_description()
print(tesla1.get_odometer())
print('battery size: ', tesla1.battery_size)
# print(car1.battery_size) # parent doesn't have this attribute
# print(car1.describe_battery) # parent doesn't have this attribute
tesla1.describe_battery()

print(' -------- Tesla 2 ----------')
tesla2 = ElectricCar('Tesla', 'Y', 20121, 90)
tesla2.describe_battery()

print(' -------- Method Overriding ----------')
car1.get_description()
tesla2.get_description()


# H/W: 9-4, 9-5












