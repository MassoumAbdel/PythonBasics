# 04/15/2023 Chapter 2

age = 16
age_str = '16' # string, text
# print('you are eligible to apply for driving license when you are ' age)
# avoid TypeError: can only concatenate str (not "int") to str
# str() function converts (numbers, boolean,...) to s string
print('you are eligible to apply for driving license when you are ' + str(age))
print('line 8: dealing with integer', age + 5)
# print('line 9: dealing with integer' age_str + 5)

# int() function converts string numbers to an integer
# print(value1,value2,...) => 'value1,value2....'
print('after 10 years you will be', int(age_str) + 10, '!')
print('after 10 years you will be ' + str(int(age_str) + 10) + '!')
print(f'after 10 years you will be {int(age_str) + 10}!')

# Using fstring
print(f'converting integer to float: {    float(age)     }')
print(f"converting 'integer' to float: {float(age)}")

# Primitive Data types: String, Integer, Boolean, Float












