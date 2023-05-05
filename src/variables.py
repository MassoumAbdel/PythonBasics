
print("============= Variables ===========")
# print is the function that returns you what you have passed to the function
# use single or double quote to enter the text
print('ABDELMOUNIM MASSOUM')
print('ABDELMOUNIM "MASSOUM"')
print("ABDELMOUNIM 'MASSOUM'")

print(555545)
print(56+65)
print(43*36)
# this is the comment line (not executable line)
# IndentationError: unexpected indent, remove spaces in the beginning of the line
print(                65)

# values covered with quotes (' ', " ") considered as String data type

# Variables: container to hold the value (storage)
age=10 # declaring the variable 'a', defining variable (set a value 10)
print(age)
age= 15 # declaring the variable 'a', defining variable (resetting the value 15)
print(age)

# NOTES for using the variables:
# name your variable with meaningful name
# rule: you can not start variable name with number, name must start with letter
# rule: no space in variable name, instead you can '_' -> my_friend
# rule: start with lower case and use lowercase letters
print(23,242,    45,"hello",True)

my_name = 'jameS broWn' # string value, text data type
my_age= 20 # integer value, numbers
am_i_cool = True # boolean data type, True/False
first_name= 'janE'
last_name= 'dOE'
full_name = first_name + ' ' + last_name
print("====================================")
print('Hello, my name is', my_name)
print('thank you, this was', my_name, 'speaking with you tonight.')
print('if you have comments please address it to', my_name)
print('I am', my_age, 'years old.')
print('i will be',my_age+5, 'years old in 5 years.')

print('-------- String Variables: built-in functions ---------')
# upper()-convert to upper case,
# lower()-lower case,
# title()- title each word
print('Hello, my name is', my_name.upper())
print('thank you, this was', my_name.title(), 'speaking with you tonight.')
print('if you have comments please address it to', my_name.lower())
print('Full name (concatenation):', first_name + ' ' + last_name.title())
print('Full name (concatenation):', full_name.title())

print('-------- Number Variables: built-in operations ---------')

print('my age is', my_age)
print('division:',my_age/5)
print('multiplication:',my_age*5)
print('floor division:',my_age//3) # f: 20/3 = 3 * f => 6.6 but floor division is => 6 (how many 3s in 20)
print('modulo:',my_age%3)  # 20/3 = 6*3+ 2 => 2 (remainder when you divide 20 to 3) it calls remainder

class1= 56
# H/W: Chapter 2: Exercises 2.8,2.9






