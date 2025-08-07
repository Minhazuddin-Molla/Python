n=int(input("Enter any number:"))
m=""
x=["0","1"]
while n>0:
    m=x[n%2]+m
    n=n//2
c=0
for i in m:
    if i=="1":
        c+=1
if c%2==0:
    print("Evil no.")
else:
    print("Not")