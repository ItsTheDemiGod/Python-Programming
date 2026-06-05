vowel = ["a", "e", "i", "o", "u"]

input_string = input("Enter a string: ")

if input_string.lower() in vowel:
    print(("the input is a vowel"))
else:
    print("the input is not a vowel")