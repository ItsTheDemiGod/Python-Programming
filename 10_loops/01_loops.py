# In python loops are used to iterate over a sequence of elements and execute a block of code for each element in the sequence . there are two types of loops in python for loop and while loop .



# for loop 

for i in range(1,6): # here loop will go from 1 to 5 
    print(i)
print() # this creates a space between the two loops for better readability
print()

# the range is in the form of range(start,stop,step) where the start in the inclusive and the stop is exclusive and the step is the increment value which is optional and by default it is 1 , even the starting is optinal and by default it is 0.


for i in range(5):
    print(i) # here the loop will go from 0 to 4 and i is called the loop variable which will take the value of each element in the sequence for each iteration of loop 



# table of 5 

for i in range(1,11):
   print("5 X" , i , "=" , 5*i) # simple way
    # print(f"5 X {i} = ",i*5)
   """ print(f"5 X {i} = {5*i} ") """
    # here we are using f strings to print the table of 5 
     





