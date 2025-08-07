a=int(input("Enter any number:"))
b=int(input("Enter any number:"))
flag=0
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        flag=1
        break
if flag==0:
    print("Co-prime numbers.")
else:
    print("Not.")
