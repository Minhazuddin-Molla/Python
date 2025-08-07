def Magic(n,s):
    if n>0:
        s+=(n%10)
        return Magic(n//10,s)
    elif n==0 and s>=10:
        return Magic(s,0)
    else:
        return s
n=int(input("Enter any number:"))
if Magic(n,0)==1:
    print("Magic no.")
else:
    print("Not")