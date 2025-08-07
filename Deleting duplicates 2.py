a=[0,1,1,2,5,4,5,7]
l=len(a)
for i in a:
    print(i)
n=int(input('Enter any no:'))
c=0
for i in range(0,l):
        if a[i]==n:
            c=c+1
            j=a[i]
            if c==2:
                for k in range(j,l-1):
                    a[k]=a[k+1]
                l=l-1
for i in range(0,l):
    print(a[i],end="  ")

