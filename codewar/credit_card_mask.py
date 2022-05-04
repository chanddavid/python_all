
def maskify(cc):
    st=''
    if len(cc)>3:
        for i,j in enumerate(cc):
            if i<(len(cc)-4):
                st+='#'
            else:
                st+=j
        return st

    elif len(cc)<=3:
        for i in cc:
            st+=i
        return st
    else:
        return ''
    
x=maskify('123')
print(x)