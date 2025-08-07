import math
def Prime(n):
   for i in range(2,int(math.sqrt(n))):
       if n%i==0:
           return False
   return True
n=int(input("Enter any no.:"))
if Prime(n):
    print("Prime")
else:
    print("Not")