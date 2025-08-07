# word="Hi I am Minhaz"
# print(len(word))
# print(len(word.center(50)))
# print(word.swapcase())
def small_dig(n):
    min=n%10
    while n!=0:
        q=n//10
        r=(n%10)/10*10
        if r>min:
            min=min
        else:
            min=r
        r=q
    return min
n=int(input("Enter any number:"))
print(small_dig(n))
# print(20*10/10)
# print(20/10*10)
# print(20//10*10)
# print(20*10//10)