def Lucky(a,x):
    l=len(a)
    if x<l:
        b=[]
        g=0
        for i in range(0,l):
            if g==x:
                g=0
                continue
            b.append(a[i])
            g+=1
        print()
        c=[]
        for i in range(0,len(b)):
            c.append(b[i])
            print(c[i],end=' ')
        x+=1
        Lucky(c,x)
    else:
        return
a=[]
n=int(input("Enter no. of terms:"))
for i in range(0,n):
    a.append(int(input("Enter any number:")))
Lucky(a,1)
