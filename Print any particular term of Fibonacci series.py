#print any particular term of Fibonacci series
a=-1
b=1
n=int(input("Enter any term:"))
for i in range(1,n+1):
    c=a+b
    if(i==n):
        print(c)
    a=b
    b=c

