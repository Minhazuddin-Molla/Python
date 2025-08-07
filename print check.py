m={'a_b_c':1,'a_b_d':2,'b_d_a':3,'d_a_b':4}
#def dict1(m):
#    for i in range(0,len(m)):
#        m.keys(i)
k=list(m.keys())
n=[]
for i in range(0,len(k)):
    n.append(k[i].split('_'))
for i in n:
    d=dict.fromkeys(i,1)
print(d)