# Iterate over a list of numbers and print only the even ones.


list = [1,2,3,4,5,6,7,8,9,10]
even = []

for i in list :
    if i %2 ==0:
        even.append(i)


print(even)
