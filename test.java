# rec={1:'a',2:'b',3:'c'}
# id1=id(rec)
# del rec
# rec={1:'a',2:'b',3:'c'}
# id2=id(rec)
# print(id1==id2)
# n=int(input("Enter any number:"))
# c=[]
# for i in range(n//2+1):
#     for j in range(n,n//2-1,-1):
#         if i+j==n:
#             c.append([i,j])
#             break
# print(c)
# def iterate(i,a,n):
#     if i==0:
#         a.append([n])
#         return iterate(i+1,a,n)
#     elif i<n:
#         a.append(partition(i,a))
#         return iterate(i+1,a,n)
#     else:
#         return a

# def partition(n,a):
#     if
def cpar(n,max):
    if n==0:
        return 1
    if n<0 or max==0:
        return 0
    return cpar(n-max,max)+cpar(n,max-1)
def parc(n):
    return cpar(n,n)
n=int(input("Enter any number:"))
print(parc(n))
