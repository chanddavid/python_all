def sep_str(st): 
    # your code here
    k=[]
    li= st.split(" ")

 
    t=len(max(li, key=len))

    for i in range(0,t):
        z=[]
        for j in range(0,len(li)):
            try:
                x= li[j][i]
                z.append(x)    
            except:
                z.append('')
        k.append(z)
    print(k) 
sep_str("The Mitochondria is the powerhouse of the cell")
