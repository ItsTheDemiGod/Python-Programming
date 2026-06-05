# Write a while loop that keeps asking the user to guess a secret number (42) until they get it right.


secret_number = 42


while secret_number != int(input("guess the secret number :")):
    print("wrong guess try again")