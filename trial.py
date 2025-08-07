import csv
fo=open("Receipt.csv","a",newline="")
fw=csv.writer(fo)
fw.writerow(["Serial No.","Item","Price(in Rs.)","Discount(%)","Amount(in Rs.)"])
n=1
sum=0
while n!=0:
    i=input("Enter name of the item:")
    p=int(input("Enter price(in Rs.):"))
    if p>=500 and p<1000:
        d=p*0.1
        d1=10
        a=p-d
    elif p>=1000 and p<1500:
        d=p*0.15
        d1=15
        a=p-d
    elif p>=1500 and p<5000:
        d=p*0.2
        d1=20
        a=p-d
    elif p>=5000:
        d=p*0.35
        d1=35
        a=p-d
    else:
        d1=0
        a=p
    fw.writerow([n,i,p,d1,a])
    sum+=a
    n=int(input("Enter next serial no.:"))
if sum>=10000:
    d2=sum*0.3
    sum=sum-d2
fw.writerow(["Total Amount(in Rs.)",sum])
fo.close()
    