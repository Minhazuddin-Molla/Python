# a=input("Enter any word:") # to input a word from user.
# w="" # to store the reverse word.
# for i in range(len(a)): # to iterate the loop from 0 to less than length of the word(length is determined by using the len() function).
#     b=a[i] # to extract letters from the word.
#     w=b+w
# if a==w:
#     print("Palindrome word.")
# else:
#     print("Not a palindrome word.")
def Palstring(a):
    if a.upper()==a[::-1].upper():
        return True
    return False
a=input("Enter any name:")
if Palstring(a):
    print("Palindrome String.")
else:
    print("Not a Palindrome String.")