o=[' ', 'One', 'Two', 'Three', 'Four','Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens=['','', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety', 'Hundred']
suffix=['','Thousand','Million','Billion']
def convert(n,w,f,c):
    if n>0:
        d=n%1000
        if d>=100 and d<=999:
            w+=o[d//100]+" "+"Hundred"+" "
            d=d%100
        if d>=20 and d<=99:
            w+=tens[d//10]+" "
            d=d%10
        if d>=1 and d<=19:
            w+=o[d]+" "
        if c>=1:
            f=w+suffix[c]+" "+f
        else:
            f=w+" "+f
        return convert(n//1000,'',f,c+1)
    else:
        return f
n=int(input("Enter the number to convert:"))
m=n
c=0
while m>0:
    c+=1
    m=m//10
if n==0:
    print("The word representation of ",n,"is: Zero")
else:
    if c>12:
        print("This program supports a maximum of 12 digit numbers.")
    else:
        print("The word representation of",n,"is:",convert(n,'','',0))