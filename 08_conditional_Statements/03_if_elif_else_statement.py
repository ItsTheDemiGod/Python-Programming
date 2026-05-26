

age = int(input("enter you age : "))

if age > 18 and age < 100 :
    print("you can drive ")
elif age ==18:
    print(" get a driving license")
elif age >0 and age < 18 :
    print( " you cannot drive")
elif age >=100:
    print(" you are dead")

else :
    print(" invalid age")
# how this is working is that the program will check the first condition if it is true then it will excute the block the code and if it is false then it will check the next condition and so on until it finds a true condition or it will execute the else block if all the conditions are false .


