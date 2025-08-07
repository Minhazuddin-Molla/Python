# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# def Zeros(n):
#     if n%10==0:
#         return 1+Zeros(n//10)
#     else:
#         return 0
# n=int(input("Enter any number:"))
# print(fact(n))
# print(Zeros(fact(n)))
def Zeros(n,i):
    if (5**i)<=n:
        return n//(5**i) +Zeros(n,i+1)
    else:
        return 0
n=int(input("Enter any number:"))
# print(fact(n))
print(Zeros(n,1))