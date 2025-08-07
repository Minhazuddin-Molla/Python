a=int(input('Enter any number:'))
def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    return False
pos=0
m=a
for i in range(0,len(str(a)) ):
    d=m%10
    if not isPrime(m):
        pos=1
        break
    m=int(str(d)+str(m//10))
if pos==0:
    print("Circular Prime")
else:
    print("Not")