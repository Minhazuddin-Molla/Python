def Happy(n, s):
    if n>0:
        s+=(n%10)**2
        return Happy(n//10, s)
    elif n==0 and s>=10:
        return Happy(s,0)
    else:
        return s
n=int(input("Enter any number: "))
if Happy(n,0)==1:
    print("Happy number.")
else:
    print("Not")