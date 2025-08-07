a=input("Enter any word:")
a1=a.split(" ");j=len(a1[0]);f=0
for i in a1:
    if len(i)!=j:
        f=1
        break
    j+=1
if f==0:
    print("Snowball String")
else:
    print("Not")