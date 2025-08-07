n=int(input("Enter any number:"))
m=n
c=0
while m>0:
    c+=1
    m=m//10
m=n
s=0
while m>0:
   s+=pow((m%10),c)
   m=m//10
if s==n:
    print("Armstrong Number.")
else:
    print("Not")
# import math
# n=int(input("Enter any number:"))
# print(n**2)
# print(pow(n,2))
# print(math.pow(n,2))
# print(math.exp(math.log(n)))
# print(math.log(math.exp(n)))
# print(math.log(math.e**n))
# print(10**(math.log10(n)))
# print(pow(10,(math.log10(n))))
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print(1 and 0)
# print(True and False)
# print(False and True)
# print(False and False)
# m=10
# n=0
# while n<10:
#     m=n
#     n=2*(n-m)
#     print(n,m,end=" ")

