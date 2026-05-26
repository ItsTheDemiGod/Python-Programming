# print("hello  " world")
"""this will cause a syntax error and print hello " world  because the interpretor will get confused as to where the termination string is ?

so if you want to print a " with the print statemennt you have to use eascape sequence like this 
"""
      
# print("hello \" world")


# one more way of printing thins is by using single quotes to enclose the string like this:

# print("hello", "world","i am good", 10) # passing multiple aruguments to the print statement  


# print("hello worlld") # by default the print stament will print the string in a new line if there are multiple print statements like this then it will print each string in a new line
# print("i am demian")

# we can change this by using the end parameter of the print statement like this:

print("hello world" )
print("i am demian", end = " ") # this means the next print statement will be printed in the same line with a space in between
print("hello")#


# if we are passing multiple arguments to the print statement then by default it will print them with a space in between but we can change this by using the sep parameter of the print statement like this:

print("hello" , "world","i am good" , 10 , sep = "-") # this will separate each arguument with a - instead of a space




print( "argument" , sep=" ",end="\n") # this is the deault print stament syantax where we pass an argument and the sep and end parameters are set to their default values which are a space and a new line character respectively .

