ch=1
while ch!=0:
    ch=int(input("Enter any choice: 0.Close 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Remainder 6.Exponent -----"))
    if ch==0:
        print("Thank You for using!!")
    elif ch<0 or ch>6:
        print("Wrong choice. Try again!!")
    else:
        a=int(input("Enter any no.:"))
        b=int(input("Enter any no.:"))
        match(ch):
            case 1:
                print(a+b)
            case 2:
                print(a-b)
            case 3:
               print(a*b)
            case 4:
                print(a/b)
            case 5:
               print(a%b)
            case 6:
               print(a**b)
