# Print the multiplication table (1–10) for a number entered by the user.

number =  int(input(" enter the number you want the table of :"))

for i in range(1,11):
    print(f" {number} x {i} = {number*i}")

