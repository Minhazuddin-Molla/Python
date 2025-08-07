a=[0,1,1,2,5,4,5,7]
l=len(a)
for i in a:
    print(a[i])
for i in range(0,l):
    n=a[i]
    for j in range(i+1,l):
        if a[j]==n:
            for k in range(j,l-1):
                a[k]=a[k+1]
            l=l-1
for i in range(0,l):
    print(a[i],end="  ")

