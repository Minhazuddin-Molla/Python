def Simp(p,r,t):
    i=p*r*t
    return i
def Comp(p,r,t):
    i=p*((1+r/100)**t)
    return i
p=int(input("Enter principal:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time:"))
Simp(p,r,t)
Comp(p,r,t)
