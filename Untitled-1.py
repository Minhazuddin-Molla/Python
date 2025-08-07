def Binary(n,x):
    if n>0:
        return Binary(n//2,x)+x[n%2]
    else:
        return ""
def Evil(n,c):
   if c<len(n):
       if n[c]=="1":
           return 1+Evil(n,c+1)
       else:
           return Evil(n,c+1)
   else:
       return 0
n=int(input("Enter any number:"))
x=["0","1"]
n=Binary(n,x)
if Evil(n,0)%2==0:
    print("Evil number.")
else:
    print("Not")