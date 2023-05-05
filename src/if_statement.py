# Programing often involves examining a set of conditions and deciding which action to take based on those conditions.
# Python's if statement allows you to examine the current state of a program and respond appropriately to that state.

# if expression
    # code to execute

cars =['toyota', 'lexus', 'bmw', 'tesla']
for car in cars:
    print(f'In this itertion car = "{car}".')
    if car =='tesla': # 'toyota' =='tesla' => false
        print('this is the code to be execute when car = tesla, i.e when the expression returns True.')
        print(f'My favourite electric car is {car.upper()}')
        print('-----------------')
    elif car == 'bmw':
            print("Elif case: this block of code executed because, car =='tesla' returned false, and car==='bmw' returned true")
            print(f'0h man {car.upper} is somthing right?')
            print('******************************')
    else:
        print('Else case: not tesla, not bmw, car=="tesla" >> False, car=="bmw" >> False, thats why we are executing this lines')
        print(f'Your current car is {car.title()}')
        print('#########################')

# conditional expressions (that returns True/False), which you can use in if or elif statement (lines):
# var == 'value1', value1 == value2, 5==4 (always false case)
#  true, false
# value1 < value2, value1 > value2,value1 <= value2, value1 != value2
# value in List, (5 in nums), 6 in range(10) -> 0,1,2,3..9,  'a' in 'book' -> False


if True:
    print('hello')

nums = [4,2,10,6,5]
if (5 in nums):
    print('5 is in the list')
elif 6 in nums:
    print('6 is in the list')
else:
    print('5 is NOt in the list')




