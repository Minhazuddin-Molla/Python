n=int(input("Enter any number:"))
dict={}
m=n
for i in range(0,10):
    m=n
    c=0
    while m>0:
        d=m%10
        if d==i:
            c+=1
            dict[d]=c
        m=m//10
print(dict)