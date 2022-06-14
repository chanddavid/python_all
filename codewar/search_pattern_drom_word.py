def func(word,pattern):
    sizeofpattern=len(pattern)

    for i,j in enumerate(word):
        if pattern in word[i:sizeofpattern+i]:
            return (i,i+sizeofpattern-1)
        
x=func("sabceabc","abc")
print(x)




def func(word,pattern):
    sizeofpattern=len(pattern)

    for i,j in enumerate(word):
        if pattern == word[i:sizeofpattern+i]:
            return (i,i+sizeofpattern-1)
        
x=func("acavabcassc","abc")
print(x)

