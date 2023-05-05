# 04/22/2023 Dictionary - data structure, each element key (word, column, field) and value (definition, value)
# each element is key-value pair, key is unique
# known with { }, key and value is separated by ':'
studentsD = {
    'student1': ['john', 23, 'tampa'],
    'student2': [['jane', 'doe'], 29, 'brooklyn'],
    'student3': ['david', 25, 'jersey city'],
}

student4 = {'name': 'raj' , 'age':  27, 'location': 'dallas'}

studentsL = [
    ['john', 23, 'tampa'],
    [['jane', 'doe'], 29, 'brooklyn'],
    ['david', 25, 'jersey city'],
    ['raj', 27, 'dallas'],
]

print('information of jane, name:', studentsL[1])

# multidimensional list (list in a list)
#
print('information of jane, city:', studentsL[1][2])
print('information of jane, last name:', studentsL[1][0][1])

customers = [
    {'customerid': 'aaaa', 'companyname': 'level up'},
    {'customerid': 'aaab', 'companyname': 'level up'},
    {'customerid': 'aaca', 'companyname': 'level up'}
]

print('###################################')

print('# CRUD with Dictionaries')

student7 = {}
student8 =dict()
student6 = {'name': 'raj' , 'age':  27, 'location': 'dallas'}

print('# Read - how to access the element, values of the dictionary ---------')
print(f"name of the student6: {student6['name'].title()}")
print(f"age of the student6: {student6['age']}")
print(f"location of the student6: {student6['location'].upper()}")

print('### Adding - (update) the element to a the dictionary --------------')
student6['last_name'] = 'patel'
print(f"After adding new key-value pair to the student6: {student6}")
print(f"After adding the last name of the student6: {student6['last_name']}")
student6.setdefault('last_name2', 'doe')
print(f"After adding setdefault new key-value pair to the student6: {student6}")

print('### Update - modifying the dictionary --------------')
student6['age'] = 30
print(f"After updating the age of the student6: {student6['age']}")

print('### Delete - removing the elements the dictionary --------------')
del student6['last_name']
print(f"After deleting new key-value from student6: {student6}")

# H/W on Problem-solving
# 1 - given string input count how many vowels used in the string (e, o , i , u, a)
# hello -> 2 vowels
#    # count = 0

# 2 - given string input count how many times each letter is used. Ignore whitespace(spaces,tabs, enters)
# hello -> result = {'h':1, 'e':1, 'l':2, '0':1}
#    # result['o'] = result['o'] + 1
#    # loop through input
#    # result.setdefault('o',1)
#    # result['o'] = result['o'] +1
for letter in 'hello':
    print(letter)





