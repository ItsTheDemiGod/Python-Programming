# Write a program to find the largest of three numbers using only if-elif-else.


num1 = float(input("enter the number 1 :"))
num2 = float(input("enter the number 2 :"))
num3 = float(input("enter the number 3 :"))

if num1> num2 and num1 > num3 :
    print("the largest number is ", num1)
elif num2 > num1 and num2 > num3 :
    print("the largest number is ", num2)
elif num3 > num1 and num3 > num2 :
    print("the largest number is ", num3)
else :
    print("all the numbers are equal")

