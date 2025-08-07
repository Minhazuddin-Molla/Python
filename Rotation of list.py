a=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter any number:"))
b=a[0:n]
for i in range(0,n):
    for j in range(1,len(a)):
        a[j-1]=a[j]
for i in range(0,len(b)):
    a[len(a)-i-1]=b[i]
print(a)