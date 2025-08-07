def binsearch(min,max,n):
    mid=(min+max)//2
    if a[mid]==n:
         return 1
    elif n<a[mid]:
        max=mid-1
        return binsearch(min,max,n)
    elif n>a[mid]:
        return binsearch(mid+1,max,n)
    else:
        return -1
a=[10,13,14,17,20,28,40,45,48,55]
n=int(input("Enter any number:"))
p=binsearch(0,9,n)
if p>-1:
    print(n,"found at index no.",p)
else:
    print(n,"Not Found")
