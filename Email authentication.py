import re
def choice():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1\nFor Signing in Type 2\nForgot Password Type 3\n"))
    if choice == 1:
       return regis()
    elif choice == 2:
       return cd()
    elif choice==3:
        return fp()
    else:
       raise TypeError

def regis():
    db = open("DATA FOR REGISTRATION", "r")
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    email = input("enter email id: ")
    password = input("enter password: ")
    valid = True
    if not (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None) :
        print('Invalid Email Id , Please try again')
        regis()
    else:
        if len(password) < 5:
            print('Password does meet the minimum length requirements of 8 characters.')
            valid = False
            regis()
        if len(password) > 16:
            print('Password should not exceed 15 characters.')
            valid = False
            regis()
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter.')
            valid = False
            regis()
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter.')
            valid = False
            regis()
        if not any(char.isdigit() for char in password):
            print('Password should have at least one number.')
            valid = False
            regis()
        if not any(char in symbols for char in password):
            print('Password should have at least one of the symbols: !@#$%^&*() ')
            valid = False
            regis()
        if valid:
            db = open("DATA FOR REGISTRATION", "a")
            db.write(email+','+password+'\n')
            db.close()
            print("Registration Sucess")
            choice()

def cd():
    e = []
    p = []
    db = open("DATA FOR REGISTRATION", 'r')
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        e.append(a)
        p.append(b)
    data = dict(zip(e, p))

    print("LOGIN")
    username = input("Please enter your email id: ")
    password = input("Please enter your password: ")

    if username in data.keys() and password in data.values():
        print("Login Sucessful!")
        return True
    else:
        print("Incorrect credentials.")
        return

def fp():
    e = []
    p = []
    db = open("DATA FOR REGISTRATION", 'r')
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        e.append(a)
        p.append(b)
    data = dict(zip(e, p))

    print("LOGIN")
    username = input("Please enter your email id : ")

    # for line in open("DATA FOR REGISTRATION","r").readlines():
    if username in data.keys() :
        password=data[username]
        print("Password is: "+ password)

    else:
        print("Incorrect credentials.")
        return

choice()




