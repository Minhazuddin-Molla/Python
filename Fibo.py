n=int(input("Enter no. of students:"))
Win={}
for i in range(n):
    k=input("Name of student:")
    no=int(input("No. of competitions won:"))
    Win[k]=no
print("Dictionary=")
print(Win)