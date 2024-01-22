mail = input("Enter email address: ")
if mail[0].isalpha() == True and mail.endswith('.com') and mail.count('@')==1:
    print("Email is valid")
else:
    print("Email is invalid")