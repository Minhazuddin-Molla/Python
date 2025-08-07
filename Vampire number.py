def Count(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    return c
n=int(input("Enter any no:"))
c=Count(n)
if c%2!=0:
    print("Not a vampire number.")
else:
    def Vampire(n,i,j):
        for i in range(n,0,-1):
            for j in range(1,int(n/2)+1):
                if Count(i)==c/2 and Count(j)==c/2 and i*j==n:
                    k=i*(10**(c/2))+j
                    if Compute(n,k):
                        return True
        return False
    def Compute(n,k):
        flag=0
        while n>0:
            d1=n%10
            while k>0:
                d2=k%10
                if d1==d2:
                    flag=1
                    break
                else:
                    k=k//10
            if flag==0:
                break
            else:
                n=n//10
        if flag==1:
            return True
        else:
            return False
    if Vampire(n,n,1):
        print("Vampire number.")
    else:
        print("Not a vampire number.")

                
                