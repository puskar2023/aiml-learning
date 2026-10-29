'''
color = input("Enter color: ")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
'''

username = input("Enter username: ")
password = input("Enter password: ")

if (username == "admin" and password == "pass"):
    print("Login successfull")
else:
    if (username == "admin"):
        print("Password is incorrect")
    else:
        print("Username not exist")