

plaintext='PASSWORD'
def ascii_encrypt(plaintext):
    cypertext=[]
    for i,j in enumerate(plaintext):
        cypertext.append(str(ord(j)+i))    
    x= list(map(int, cypertext))

    print(type(x))
    for i in x:
        print(chr(i),end="")
ascii_encrypt(plaintext)




# or
plaintext='PASSWORD'
def ascii_encrypt(plaintext):   
    return ''.join(chr(ord(j)+i) for i,j in enumerate(plaintext))
ascii_encrypt(plaintext)

