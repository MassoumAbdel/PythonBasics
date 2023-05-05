# H/W: Fuzz/Buzz   . /fuzz_buzz.py
# create condition that prints 'Fuzz' if number if dividable by 3, returns 'Buzz' if number id dividable by 5

# returns 'FuzzBuzz' if the number dividable by 15
# Sample outputs
# num = 3 # output 'Fuzz' -> True/False -> Pass/Fail
# num = 27 # output 'Fuzz' -> True/False -> Pass/Fail
# num = 10 # output 'Buzz' -> True/False -> Pass/Fail
# num = 30 # output 'FuzzBuzz' -> True/False -> Pass/Fail
# num = 45 # output 'FuzzBuzz -> True/False -> Pass/Fail
# num = 100 # output 'Buzz' -> True/False -> Pass/Fail
# num = 0 # output 'Not Valid Entry, for any input less than 3' -> True/False -> Pass/Fail
# num = 'a' # output 'Not Valid Entry, for any input other than integer' -> True/False -> Pass/Fail
# num = '' # output 'Not Valid Entry, for any input other than integer' -> True/False -> Pass/Fail
# num = '/t' # output 'Not Valid Entry, for any input other than integer' -> True/False -> Pass/Fail

# for num in range(1, 21):
#   string = ""
#   if num % 3 == 0:
#       string= string + "Fuzz"
#   if num % 5 == 0:
#       string= string + "Buzz"
#   if num % 5 != 0 and num % 3 != 0:
#        string = string + str(num)
#        print(string)

def fuzz_buzz(num):
    # num.isalpha() # return True if num is alphabetic character, works for sting only
    # num.isnumeric()
    result = ""
    if num == 0 or not isinstance(num,int):
        result= (f'You Entry "{str(num)}," is Not Valid')
    elif num % 15 == 0:
        result = "Fuzz"  + "Buzz"
    elif num % 5 != 0 and num % 3 != 0:
        result = result + str(num)
    elif num % 5 == 0:
        result = result + "Buzz"
    elif num % 3 == 0:
        result = result + "Fuzz"

    return result

print(fuzz_buzz(15))
print(fuzz_buzz(3))
print(fuzz_buzz(''))
print(fuzz_buzz(1))
print(fuzz_buzz(0))
print(fuzz_buzz(5))
print(fuzz_buzz('a'))
print(fuzz_buzz(45))
print(fuzz_buzz('|t'))
print(fuzz_buzz(13))

print(fuzz_buzz(15) == 'FuzzBuzz')
print(fuzz_buzz(3) == 'Fuzz')
print(fuzz_buzz(5) == 'Buzz')
print(fuzz_buzz(45) == 'FuzzBuzz')

# assert is builtin python statement that verifies the actual result with expect
# if fails (expression returns false) code execution stops

