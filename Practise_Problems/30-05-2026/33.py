# Build a login check: if username is 'admin' and password is '1234', print 'Access granted', else 'Denied'.


username_0 = "admin"
password_0 = "1234"

username = input("enter the username :")
password = input("enter the password :")

if username == username_0 and password == password_0 :
    print("Access granted")
else:
    print("denied")