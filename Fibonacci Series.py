n=int(input("Enter the no.of terms of series:"))
a=-1
b=1
c=0
for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c
