# in this file we want to have a execution only (Classes)

class car:
    """ Blueprint to represent the general car."""

    # constructor
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year = year
        self.odmeter_reading = 0 # default value
        # self.__odmeter_reading = 0 this means hidden attribute from the object, private

    def get_description(self):
        """ summary of car details, usually you have return statement"""
        print(f"Details of the car\n\tMake/Model/Year: {self.make.title()}/{self.model.upper()}/{self.year}")

    def get_odometer(self):
        return f'Current milage: {self.odmeter_reading}'

    def set_odometer(self, milage):
        """ Updates the odometer reading to given milage"""
        if milage > self.odmeter_reading:
            self.odmeter_reading = milage
        else:
            print(f"Invalid milage wa entered for odometer! value entered: {milage}")

    def increment_odometer(self, miles):
        """ Add trip miles to your overalll milage of the car."""
        print(f" adding {miles} miles to your odometer reading...")
        if miles > 0:
            self.odmeter_reading += miles
        else:
            print(f"Miles should be a positive number! value entered: {miles}")

