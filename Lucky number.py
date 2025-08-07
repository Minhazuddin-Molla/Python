def Lucky(a,n,c,i):
    if i<len(a):
        n.append(a[i])
        c=c+1
        if c+1==i:
            return Lucky(a,n,i+2,j)
        else:
            return Lucky(a,n,i,j)
    elif a==n:
        return n
    else:
        return Lucky(n,[],0,j+1)
a=[]
n=int(input("Enter no. of terms:"))
for i in range(0,n):
    a.append(int(input("Enter any number:")))
new=[]
f=Lucky(a,new,0,1)
for i in f:
    print(f[i],end=" ")
