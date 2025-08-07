def Lucky(a,j,k):
    n=[]
    j+=k
    for i in range(0,len(a)):
        if i!=j:
            n.append(a[i])
        else:
            j+=k
    if a==n:
        return n
    else:
        return Lucky(n,-1,k+1)
a=[]
n=int(input("Enter no. of terms:"))
for i in range(0,n):
    a.append(int(input("Enter any number:")))
f=Lucky(a,-1,2)
for i in f:
    print(i,end=" ")
