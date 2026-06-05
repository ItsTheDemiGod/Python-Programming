# Iterate through a dictionary and print each key-value pair in the format 'key → value'.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

for key,value in my_dict.items():
    print(f"{key} --> {value}")


print(my_dict.items())