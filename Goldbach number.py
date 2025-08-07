import math
def goldbach(n,i,j):
    if i<=n and i>=3:
        if j>=3 and j<=n/2:
            if i+j==n and Prime(i) and Prime(j):
                return True
            else:
                return goldbach(n,i,j+1)
        else:
            return goldbach(n,i-1,3)
    else:
        return False
def Prime(n):
   for i in range(2,int(math.sqrt(n))+1):
       if n%i==0:
           return False
   return True
n=int(input("Enter any number:"))
if goldbach(n,n,3):
    print("Goldbach no.")
else:
    print("Not")