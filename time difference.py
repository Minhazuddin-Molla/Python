def convert(n):
    if n%10==1:
        n=n//10+1200
        n=n//100*60+n%100
    else:
        n=n//10
        n=n//100*60+n%100
    return n
a=int(input("Enter any time in format(hhmm0 for a.m. and hhmm1 for pm):"))
b=int(input("Enter any time in format(hhmm0 for a.m. and hhmm1 for pm):"))
a=convert(a)
b=convert(b)
c=0
if a>b:
    c=a-b
else:
    c=b-a
print("Difference of time:",c//60,"hours",c%60,"minutes")