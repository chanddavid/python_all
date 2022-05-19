def sep_str(st): 
    # your code here
    y=[]
    li= list(st.split(" "))

    z=[]
    # t=len(max(li)) 
    t=len(max(li, key=len))
    for items in li:
        if t!=len(items):
            x=t-len(items)
            items=items[:]+" "*x

            y.append(items) 
        else:
            y.append(items)

    for i in range(0,len(y)):        
        x= [item[i] for item in y ]
  
        z.append(x)        
    print(z) 

sep_str("The Mitochondria is the powerhouse of the cell")