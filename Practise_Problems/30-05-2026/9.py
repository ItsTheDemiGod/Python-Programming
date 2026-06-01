# Create a dictionary with keys 'name', 'age', and 'city'. Print each value individually.

person = {
    "name" : "demian",
    "age" : 21,
    "city" : "simdega"
    }
print(person.keys())
print(person.values())
print(person.__getitem__("name"))
print(person.get("name")) # we use .get() function to get the value of that key in the dictionary
print(person.get("age"))
print(person.get("city"))