a=[]
print("Enter 10 numbers: ")
for i in range(0,10):
    a.append(int(input()))
for i in range(0,10):
    print(a[i],end=" ")
for i in range(0,9):
    for j in range(0,9-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print()
print("The numbers in sorted order:")
for i in range(0,10):
    print(a[i],end=" ")