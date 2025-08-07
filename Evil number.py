def Binary(n,c):
    if n>0:
        return (n%2)*c+Binary(n//2,c*10)
    else:
        return 0
def Evil(n):
    if n>0:
        if n%10==1:
            return 1+Evil(n//10)
        else:
            return Evil(n//10)
    else:
        return 0
n=int(input("Enter any number:"))
n=Binary(n,1)
if Evil(n)%2==0:
    print("Evil number.")
else:
    print("Not") 