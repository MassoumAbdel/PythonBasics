# Chapter 4 Looping: Interative actions

magicians = ['alice', 'david', 'caroline']

# for each loop
for abc in magicians:   # new variable abc created, scope is for loop block
        print(f'magician: {abc}')
        print('hello')
        print(abc, '------------')

print(abc)    # out of scope always will print the last one
print('byeeee')

# range(startingNumber, endingNumber, steps)
# NOTE: range does not return a list, you need to use list() functions
# to see the result in a list

# range(10,20,2) -> 10,12,14,16,18
# range(5) -> range(0,5,1) -> 0, 1, 2, 3, 4
# range(16, 21) -> range(16,21,1) -> 16, 17, 18, 19, 10

print(' ####### Working with number with range() -------------')
print(f'range(): {list(range(5))}')

print(f' #  # using range in loop')
for num in range(16,21):
        print(f'num: {num}')

print(f'********* Completed **********')
print(f' #  #  Square with range **********')
# Exercise: create a list of squares of number from 101 to 110 (inclusive)
squares =[]
for num in range(101,111):
        squares.append(num**2)
print(squares)

# solution 2
# for num in range(101,111):
#        print(f'The square of {num} is: {num*num}')

# solution 3 comprehension
# squares = [value **2 for value in range(101,111)]

# find the sum of numbers 55 to 95
total = 0
for num in range(55, 96):
        total = total + num
        # or
        # total+= num
print(total)

print('######  Slicing in the list -------------')
nums= [4, 23, 6, 0, -11, 233,4231]
print(nums[2:5]) # this includes indexes 2, 3, 4
print(nums[2:]) # this includes all indexes starting from 2
print(nums[:5]) # this includes all indexes up index 5 (not including 5)
print(nums[:]) # this includes all indexes
nums_2_5 = nums[2:5]
nums_2_end = nums[2:]
nums_start_5 = nums[:5]
nums_copy = nums[:] # created new list (object) by copying in list
print(f'nums_copy: {nums_copy}')

nums_copy2 = nums # created additional reference to the same object
print(f'nums_copy2: {nums_copy2}')
print(f'original copy: {nums}')
print('---------------------')
nums_copy.append(555)
nums.append(666)
nums.append(777)
nums.insert(0,897)
print(f'nums_copy after change: {nums_copy}')
print(f'nums_copy2 after change: {nums_copy2}')
print(f'nums after change: {nums}')

print('---------------------')

print(min(nums))
print(max(nums))
print('---------------------')

for numbers in nums[3:]:
        print(numbers)
print('---------------------')

for numbers in nums[2:7]:
        print(numbers)
print('---------------------')



