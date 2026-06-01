# Demonstrate all 7 arithmetic operators (+, -, *, /, %, **, //) using two variables a=17 and b=5.

a = 17
b = 5

operation = input("ente the operation you want to perform(=,-,/,*,**,//) : ")

if operation == "+":
    print(f"a+b:{a+b}")
elif operation == "-":
    print(f"a+b:{a-b}")
elif operation == "-":
    print(f"a+b:{a*b}")
elif operation == "*":
    print(f"a+b:{a*b}")
elif operation == "**":
    print(f"a+b:{a**b}")
elif operation == "/":
    print(f"a+b:{a/b}")
elif operation == "//":
    print(f"a+b:{a//b}")
else :
    print("invalid operation")