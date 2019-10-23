userNames = "Death, Todd, Demetrius, larry"
passWord ="daorspsw"
passWord2 ="drowssap"
passWord3 =""
uninput = input("enter your username")
if uninput in userNames:
    pwinput =input("enter your password")
    
    if passWord == pwinput:
        print("you got in")
    elif passWord2 == pwinput:
        print("you got in")
    elif passWord3 == pwinput:
        print("you got in")
    else:
        print("you didn't got in")
        
else:
    print("you didn't get in")
