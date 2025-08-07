def perfect(n,c):
    if c<=n//2:
        if n%c==0:
            return c+ perfect(n,c+1)
        else:
            return perfect(n,c+1)
    else:
        return 0
n= int(input("Enter any number:"))
if perfect(n,1)==n:
    print("Perfect number.")
else:
    print("Not")