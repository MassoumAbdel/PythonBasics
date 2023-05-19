# Chapter 10: Read Files (txt)

# with open(filepath) as file_object:
#     file_contents = file_object.read() # option 1 - get the whole content

#     file_contents = file_object.readlines() # option 2 - get all lines in a list

#     file_contents = file_object.readlines() # returns line 1
#     file_contents = file_object.readlines() # returns line 2
#     file_contents = file_object.readlines() # returns line 3

# file_lines[1] -> this returns the second line of file (just like a list)
# print(file_contents)

filepath_txt = "fruits.txt" # or you could give the full path of file
                    # example ../../data/fruits.txt
with open(filepath_txt) as file_object:
     file_contents = file_object.read()

     # or you could print line by line from the file by using for loop
     # for fruit in file_object:
     #      print(f"Current loop fruit: {fruit.strip()}")
     # strip() = just to remove line space between lines
print("-------- Now printing the contents ----------")
print(file_contents)





