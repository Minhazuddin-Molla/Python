def Count(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    return c
def Compute(n,k):
    flag=0
    a=list(str(k))
    while n>0:
        d=n%10
        for i in a:
            if i==str(d):
                flag=1
                break
        if flag==0:
            return False
        n=n//10
    return True
n=int(input("Enter any no:"))
c=Count(n)
if c%2!=0:
    print("Not a vampire number.")
else:
    def Vampire(n):
        for i in range(1,n//2+1):
            if n%i==0:
                j=n/i
                if Count(i)==c/2 and Count(j)==c/2:
                    k=i*(10**(c/2))+j
                    if Compute(n,k):
                        return True
        return False
    if Vampire(n):
        print("Vampire number.")
    else:
        print("Not a vampire number.")