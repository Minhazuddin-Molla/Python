def Binary(n,x):
    if n>0:
        return Binary(n//2,x)+x[n%2]
    else:
        return ""
def Evil(n):
    if n>0:
        if n%10==1:
            return 1+Evil(n//10)
        else:
            return Evil(n//10)
    else:
        return 0
n=int(input("Enter any number:"))
x=["0","1"]
n=(int)(Binary(n,x)) 
if Evil(n)%2==0:
    print("Evil number.")
else:
    print("Not") 