n=int(input("Enter any number:"))
se=0
so=0
m=n
while m>0:
    d=m%10
    if d%2==0:
        se+=d
    else:
        so+=d
    m=m//10
if se==so:
    print("Lead number")
else:
    print("Not a lead number")
