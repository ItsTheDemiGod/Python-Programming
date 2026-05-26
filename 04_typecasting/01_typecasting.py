# typecasting is the process of converting a value from one data type to another. 
"""Python provides built-in functions for typecasting:
int(): Converts to integer.
float(): Converts to float.
str(): Converts to string.
bool(): Converts to boolean."""

age = 20 
# print(type(age))

name = "demian"
# print(type(name))

cgpa = 3.2
# print(type(cgpa))
is_student = True
# print(type(is_student))

# to typecaste a value we do this , 
age = str(age) # this will conver the int datatype to str datatype

# print(type(age))


a = 20
print(type(a)) # this will print <class 'int'> because a is an integer variable
b = "20"
print(type(b)) # this will print <class 'str'> because b is a string variable

# same value but different data types

c = True 

print(type(c)) # this will print <class 'bool'> because c is a boolean variable

d = str(c)
print(type(d)) # this will print <class 'str'> because d is a string variable

"""f = "@20"
print(type(f)) # this will print <class 'str'> because f is a string variable

g = int(f) # this will cause a ValueError because f cannot be converted to an integer since it contains a non-numeric character (@)
print(type(g)) # this will throw an error and will not print anything because the previous line will raise a ValueError and stop the execution of the program. since it a interpretored language it will stop the execution as soon as it encounters an error."""



pi = 3.14

int_pi = int(pi) # this is return the intergal value of pi

print(int_pi)