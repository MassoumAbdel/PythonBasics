# Object - abstract data
# An object is simply a collection of data (variables) and methods (functions).

# Data Structure: List [v1,v2], Tuple (v1,v2), Set {v1,v2}, Dictionary {key1:v1, key2:v2}
# We will learn followings for each data structure:
# difference than other DS,
# Operations: create, read, update, delete  (CRUD)
# Each DS has mostly used builtin functions

# List - list of values (similar data types) separating with comma
# list covered with  square brackets -> [value1, value2,...]

print('# Create ******************')
friends = []
nums = list()
my_info = ['john', 'doa', 30, 'dubai', True, '04/15/1993']
cities = ['brooklyn', 'manhattan', 'los angeles']

print(my_info)
print(cities)
print(friends)
print('nums:', nums)

print('# Read ******************')
print(my_info[0]) # 'john'
print(f'First element of my_info list is : {my_info[0]}') # 'john'
print(f'First element of my_info list is : {my_info[0].title()}') # 'John'
print(f'The last element cities list is : {cities[-1].title()}') # 'Los Angeles'
print(f'The last element cities list is : {cities[2].title()}') # 'Los Angeles'
print(f'{my_info[0].title()} will be {  my_info[2] + 5   } years old 5 years') # 'los angeles'

print('### Creating a list from user input ---------')
name = input('Enter your name: ') # user input the value then that value will be saved as name='value'
age = int(input('Enter your age: ')) # option 1
# option 2
# age = input('Enter your age: ')
# age = int(age) - right side of the equal sign will be executed first and set a new value to age variable

city = input('Enter your city: ')
user_info = [name, age, city]

print(f'User info: {user_info}')
print(f'Name of user: {user_info[0]}')
print(f'Age of user, 2 years ago: {user_info[1] - 2}')
print(f'Location fo user: {user_info[2]}')

print(' ####  UPDATE *******************')
print('original list ', cities) # ['brooklyn', 'manhattan', 'los angeles']
print("# Inserting the elements to the list -----------")
cities.insert(1,'houston')
print('updated list', cities) # ['brooklyn', 'houston', 'manhattan', 'los angeles']
print("# updating the existing element value -----------")
cities[2]= 'new york' # update manhattan to new york
print('updated manhattan in list', cities) # ['brooklyn', 'houston', 'new york', 'los angeles']
print('updated manhattan', cities[2])
print('#######  ADD new element to the end of the list (append) --------------')
cities.append('seattle') # mostly used
print(f'new city added to the list: {cities}') # ['brooklyn', 'houston', 'new york', 'los angeles', 'seattle']
print(f'new city added to the list: {cities[-1]}')
print(f'new city added to the list: {cities[len(cities)-1]}')

print('index of houston', cities.index('houston'))
print('counting the elements of cities list',len(cities))

print('########## DELETE elements')
print('original before deleting:', cities) # ['brooklyn', 'houston', 'new york', 'los angeles', 'seattle']
del cities[0] # just removes, only delete action
print('after deleting the first element with del:', cities) # ['houston', 'new york', 'los angeles', 'seattle']
cities.pop() # remove and return item at index (default last)
print('after deleting the first element with pop():', cities) # ['houston', 'new york', 'los angeles']
cities.pop(1) # remove and return item at index (default last)
print('after deleting the first element with pop():', cities) # ['houston', 'los angeles']
delete_city= cities.pop(1) # remove and return item at index (default last)
print('deleting_city:', delete_city) # ['los angeles']

cities.append('new york')
print('add new york :', cities) # ['los angeles', 'new york']

cities.remove('new york')
print('after deleting the first element with remove():', cities) # ['houston']

print('hello'.title())

# 04/16/2023

print('########  Sorting in lists -----------------------------')
cars=['lexus', 'bmw', 'tesla', 'toyota']
print(f'car list:{cars}')

print(' ########## Temporary sorting of list with sorted() ----------------')
print(f'sorted list with sorted() list:{sorted(cars)}')
print(f'list after sorted() list:{cars}')
print(f'sorted list with sorted(reserve=True):{sorted(cars, reverse=True)}')
print(f'list after sorted() list:{cars}')
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars, reverse=True)
print(f'sorted_cars_asc:{sorted_cars_asc}')
print(f'sorted_cars_desc:{sorted_cars_desc}')

print(' ########## Permanent sorting of list with sort() ----------------')
cars.sort() # permanent sorting by default in ascending order.
# cars.sort(reverse=True) - permanent sorting in descending order
# print(f' sorted cars list with sort(reverse=True):{cars}')
print(f'sorted cars list with sort() list:{cars}')
cars.append('honda')
print(f'cars after append:{cars}')

# problem solving: you have huge list of integer,
# how you can find smallest and largest number
nums =[4, 23, 6, 8, -11, 32,343]
# solution 1
nums.sort()
smallest_num= nums[0]
largest_num= nums[-1]

# solution2 : you could do it in 2 lines
# smallest_num= sorted(nums)[0]
# largest_num= sorted(nums)[-1]

print(' ########## reversing the list with reverse() ----------------')
nums2 = [2, 5, 1, 0, -55, 100]
print(f'original list: {nums2}')
nums2.reverse()
print(f'reverse list: {nums2}')

# IndentationErrors, SyntaxError, TypeError, IndexError, NameError
# Avoiding Index Errors When Working with Lists
# Ex from the list num2 has only until index 5
print(f'out of range index num2 [6]: {nums2[6]}')











