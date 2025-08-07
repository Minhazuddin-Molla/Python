# n=int(input("Enter any number:")) # to enter a number from user
# c=0 # it is called counter, used for counting factors
# values=range(1,n+1) # to store values from 1 to n by using function range()
# for i in values: # to iterate the loop from 1 to n
#     if n%i==0 :
#         c+=1
# if c==2:
#     print("Prime number")
# else :
#     print("Not a prime number.")
def Prime(n,i):
    if i<n:
        if n%i==0:
            return False
        else:
            return Prime(n,i+1)
    else:
        return True
n=int(input("Enter any number:"))
if Prime(n,2):
    print("Prime no.")
else:
    print("Not")