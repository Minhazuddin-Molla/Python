n=int(input("Enter any no.:"))
flag=0
for i in range(1,n):         
    if(i*(i+1)==n):
        flag=1
        break
if flag==1:
    print("Pronic no.")
else:
    print("Not")