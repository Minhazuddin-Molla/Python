import csv
fileobject=open("Student.csv","a+",newline="")
filewriter=csv.writer(fileobject)
filewriter.writerow(["Name","Computer Marks"])
a=[];b=[]
for i in range(0,5):
    print("Record",i)
    b.append((input("Enter name:")))
    a.append(int(input("Enter computer marks:")))
for i in range(0,4):
    for j in range(0,4-i):
        if a[j]<a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            temp1=b[j]
            b[j]=b[j+1]
            b[j+1]=temp1
for i in range(5):
    filewriter.writerow([b[i],a[i]])
fileobject.close()
            