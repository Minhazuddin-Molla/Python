n=int(input("Enter any number:"))
a=[]
m=n
c=0
s=0
while m>0:
    c+=1
    a.append(m%10)
    m=m//10
a=a[::-1]
while s<n:
    s=0
    for i in a:
        s+=i
    for i in range(0,c-1):
        a[i]=a[i+1]
    a[c-1]=s
if s==n:
    print("Keith Number.")
else:
    print("Not")
