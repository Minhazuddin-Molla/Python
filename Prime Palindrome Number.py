a=int(input("Enter any no.:"))
def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
         return True
    return False
def isPalindrome(n):
    m=n
    s=0
    while m>0:
        s=s*10+(m%10)
        m=m//10
    if n==s:
        return True
    return False
if isPrime(a) and isPalindrome(a):
    print("Prime Palindrome")
else :
    print("Not")
   

      

