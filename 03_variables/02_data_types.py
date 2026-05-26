# python has several built-in data types that allow us to store and manipulate different kinds of data. some of the most commonly used data types in python include:

# 1. int : used to represent whole numbers (both positive and negative) without a decimal point. for example: 1, -5, 0, 100.
# 2. float : used to represent numbers with a decimal point. for example: 3.14, -0.5, 0.0, 2.71828.
# 3. str : used to represent sequences of characters (text). strings are enclosed in either single quotes (' ') or double quotes (" "). for example: 'hello', "world", 'python programming'.
# 4. bool : used to represent boolean values, which can be either True or False. boolean values are often used in conditional statements and logical operations.
# 5. list : used to represent an ordered collection of items, which can be of different data
# 6. tuple : used to represent an ordered collection of items, similar to lists but immutable (cannot be changed after creation).
# 7. dict : used to represent a collection of key-value pairs, where each key is unique and maps to a corresponding value. for example: {'name': 'demian', 'age': 20, 'cgpa': 3.4}.
# 8. set : used to represent an unordered collection of unique items. for example: {1, 2, 3, 4}.
    


name = "demian " # this is a string variable 
age = 21 # this is an integer variable 
cgpa = 3.4 # this is a float variable
is_student = True # this is a boolean variable
lis = [1,2,3,4] # this is a list variable
tup = (1,2,3,4,4) # this is a tuple variable
dict = {"name": "demian", "age": 21, "cgpa": 3.4} # this is a dictionary variable
set = {1,2,3,4,4,4} # this is a set variable


print(name)
print(type(name)) # this will print <class 'str'> because name is a string variable
print(age)
print(type(age)) # this will print <class 'int'> because age is an integer variable
print(cgpa)
print(type(cgpa)) # this will print <class 'float'> because cgpa is a float variable
print(is_student)
print(type(is_student)) # this will print <class 'bool'> because is_student is a boolean variable
print(lis)
print(type(lis)) # this will print <class 'list'> because lis is a list variable
print(tup)
print(type(tup)) # this will print <class 'tuple'> because tup is a tuple variable
print(dict)
print(type(dict)) # this will print <class 'dict'> because dict is a dictionary variable
print(set) # this will only print unique values in the set, so it will print {1, 2, 3, 4} instead of {1, 2, 3, 4, 4, 4}
print(type(set)) # this will print <class 'set'> because set is a set variable