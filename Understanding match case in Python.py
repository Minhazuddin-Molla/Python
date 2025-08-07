#Understanding match case in Python
ch=int(input("Enter any number:"))
match ch:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case _:
        print("Case not found") # Default case in Python is written as case _
# Here break statement is not necessary like in Java, C++, etc.