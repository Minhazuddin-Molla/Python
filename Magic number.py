n=int(input("Enter any no.:"))
m=n
s=0
while m>0:
    b=m%10
    s=s+b
    m=m//10
    if m==0 and s>=10:
        m=s
        s=0
if s==1:
    print("Magic no.")
else:
    print("Not")
