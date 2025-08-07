# def Base(n,c):
#     if n>0:
#         return Base(n//c,c)+x[n%c]
#     else:
#         return ""
# x=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
n=int(input("Enter any decimal no.:"))
# c=int(input("Enter the base in which u want to convert:2.Binary 8.Octal 9. Nonal 16. hexadecimal and so on.: "))
# print("The number",n,"in the new base:",Base(n,c))
bin=0
c=1
while n>0:
    d=n%2
    bin+=d*c
    c*=10
    n=n//2
print(bin)