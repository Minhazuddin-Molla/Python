def permutations(word):
    if len(word)==1:
        return [word]
    perm=permutations(word[1:])
    char=word[0]
    z=[]
    for i in perm:
        for j in range(len(i)+1):
            z.append(i[j:]+char+i[:j])
    return z
word=input("Enter any word:")
print(permutations(word))