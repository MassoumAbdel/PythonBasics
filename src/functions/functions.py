# Chapter 8 : Functions
# function name is the summary of action it does
# keep your functions to do specific task only (recommended)
# function names should not have space, use '_' (underscore) instead
# docstring to describe functions, parameters and give example of execution
def greet_user():
    """ Display a simple greetings """
    # pass # do nothing but keeps the syntax of the functions
    print('hello!!')

def greet_user_by_name(name):
    """ Display a simple greetings using the name."""
    print(f'hello, {name.title()} !!')


def thank_you_by_name(name, years):
    """ Display thanks you message."""
    print(f'Thank you {name.title()} for being with us {years} years')

print('I am free of any function')




