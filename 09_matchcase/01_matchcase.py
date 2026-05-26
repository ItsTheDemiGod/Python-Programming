# match case statements are an alternative to if-else statement in python and they are used to match a value against a patter and execute a block of code if the pattern matches the value . they are introduced in python 3.10 and they are similar to switch case statements in other programming languages .


lucky_number = int(input("enter your lucky number : "))

match lucky_number:
    case 1:
        print("you are lucky number 1")
    case 2:
        print("you are lucky number 2")
    case 3:
        print("you are lucky number 3")
    case 4:
        print("you are lucky number 4")
    case __:
        print("you are not lucky number 1,2,3,4")


    # how this is working is that we are prompting the user to enter the lucky number and then we are using the match case statment to match the lucky number with the cases and if it matches then it will execute the block of code for that case and if it doesnt match any of the cases the it will execute the block of code for the default case which is represented by __ . 
    