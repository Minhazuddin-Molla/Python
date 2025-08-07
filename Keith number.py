def Count(n):
    if n>0:
        a.append(n%10)
        return 1+Count(n//10)
    else:
        return a,0
def Keith(n,c,s):
    if s<n:
        s=0
        for i in range(c,c-3,-1):
            s+=a[i]
        a.append(s)
        return Keith(n,c+1,s)
    else:
        return s
a=[]
n=int(input("Enter any number:"))
m=n
c=Count(n)-1
while c>=0:
    a.append(m//(10**c))
    m=m%(10**c)
    c=c-1
if Keith(n,Count(n)-1,0)==n:
    print("Keith number.")
else:
    print("Not")