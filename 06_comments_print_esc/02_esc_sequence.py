# escape sequence is used to represent special characters in a string that cannot be directly included. It is denoted by a backslash (\) followed by a specific character. Here are some common escape sequences in Python:
"""1. \n : represnts new line 
2. \t : represents a tab
3. \\ : respresents a backlash
4. \' : respresents a single quote
5. \" : represents a double quote
etc
"""


# print("hello
# world") # suposse you want to write world in a new line and you try to do this then it will cause a syntax error . to do this correctly we have to use escape sequence \n to represent a new line character like this :

print("hello\nworld")# this will print world in the new line 
print("hello\tworld") # this will print world after a tab space from hello
print("hello\\world") # this will print hello\world because \\ is used to represent
print('I\'m a student') # this will print I'm a student because \' is used to represent a single quote character
print("She said, \"Hello!\"") # this will print She said, "Hello!" because \" is used to represent a double quote character
