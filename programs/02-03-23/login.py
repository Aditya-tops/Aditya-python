d1={
    'Name':'User',
    "E-mail":"user@gmail.com",
    'Pswd':'user123'
    }

username=input("Enter username/email id: ")
pswd=input("Enter Password: ")

if username==d1['E-mail'] and pswd==d1['Pswd']:
    print("Login Success")
else:
    print("Acess Denied")