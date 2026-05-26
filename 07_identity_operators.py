# identity operators are used to compare the memory location of two objects . 
# we use is and is not for this purpose 


# example
a = 10
b = 12

print ( a is b ) # this will return false because a and b are different values in the memory
print ( a is not b ) # this will return true 


c = a

print ( a is c ) # this will true because a and c are same values in the memory 
