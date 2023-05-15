# 9-1

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name= name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        print(f'{self.name} is open now!!')

    def describe_restaurant(self):
        print(f'{self.name} is fine {self.cuisine_type} restaurant.')

    def set_number_served(self,num_customers):
        print(f'Setting the number served to {num_customers}...')
        self.number_served = num_customers


    def increment_number_served(self, num_customers):
        """ Add num_customers to current number_served
        :param num_customers: number to be increment by
        """
        print(f'Increment the number served by {num_customers} ...')
        self.number_served += num_customers
        print(f'Current number served {self.number_served}')


restaurant1 = Restaurant('Silk Road', 'Uzbek')
print(f'Number of customers server so far: {restaurant1.number_served}')
restaurant1.number_served = 2
print(f'Number of customers server so far: {restaurant1.number_served}')
restaurant1.set_number_served(10)
print(f'Number of customers server so far: {restaurant1.number_served}')
restaurant1.increment_number_served(5)


