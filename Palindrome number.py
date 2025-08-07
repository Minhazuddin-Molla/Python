# n=int(input("Enter any number:"))
# m=n
# s=0
# while m>0:
#     s=s*10+m%10
#     m=m//10
# if n==s:
#     print("Palindrome number.")
# else:
#     print("Not a palindrome number.")
def pal(n,c):
    if n==0:
        return c
    c=c*10+n%10
    return pal(n//10,c)
n=int(input("Enter any number:"))
if n==pal(n,0):
    print("Palindrome number.")
else:
    print("Not a palindrome number.")
