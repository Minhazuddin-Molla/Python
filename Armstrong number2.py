def Count(n):
    if n>0:
        return 1+Count(n//10)
    else:
        return 0
def Armstrong(n):
    if n>0:
        return (n%10)**c+Armstrong(n//10)
    else:
        return 0
n=int(input("Enter any no."))
c=Count(n)
if Armstrong(n)==n:
    print("Armstrong no.")
else:
    print("Not.")
