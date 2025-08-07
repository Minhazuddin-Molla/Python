def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def Strong(n):
    if n>0:
        return fact(n%10)+Strong(n//10)
    else:
        return 0
n=int(input("Enter any number:"))
if Strong(n)==n:
    print("Strong number")
else:
    print("Not")