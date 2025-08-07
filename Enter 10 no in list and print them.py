a=input("Enter any name:")
b=input("Enter any name:")
x=[]
for i in a:
    if i not in b:
        x.append(i)
for j in b:
    if j not in a:
        x.append(j)
print(x)