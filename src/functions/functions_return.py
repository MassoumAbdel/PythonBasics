# Chapter 8: the return statement takes a value from inside a function and sends it back
# to the line that called the functions
# Returns values allow you to move much of your program's grunt work into
# functions, which can simplify the body of your body

# get data/info (getters); usually these kind of functions have return value,
    # you can assign the function to a variable, treat as a value
# get data/info (setters); create/update data/info in db,code,variable (applies logic in the functions)
def get_full_name(first_name, last_name, middle_name=''): # middle name is optional parameter, default value is empty space
    if middle_name != '':
        return f"{first_name} {middle_name} {last_name}".title()
    else:
        return f"{first_name} {last_name}".title()



def print_all_names(names):
    print("***** print all of names (List) *****")
    for name in names:
        print(name)










