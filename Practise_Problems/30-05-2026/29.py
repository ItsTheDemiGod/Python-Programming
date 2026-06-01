# Grade a student: 90–100 = A, 80–89 = B, 70–79 = C, 60–69 = D, below 60 = F.


marks = int(input("enter the marks for the student :"))


if marks < 60 :
    print("grade F")
elif 60 <= marks <= 69 :
    print("grade D")
elif 70 <= marks <= 79 :
    print("grade C")
elif 80<=marks<=89:
    print("Grade  B")

elif 90 <= marks <= 100:
    print(" Grade A ")
else :
    print("invalid marks ")