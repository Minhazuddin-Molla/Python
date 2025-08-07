a=input("Enter any name:")
a=" "+a
l=len(a)
for i in range(0,l):
    if a[i]==" ":
        print(a[i+1],end=".")