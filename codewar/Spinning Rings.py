    # inner = inner_max
    # outer = 1
    # count=1
    # while True:
    #     print(inner,outer)
    #     if inner==outer:
    #         break
    #     if inner == 0:
    #         inner = inner_max
    #     if outer == outer_max:
    #         outer = 0
        
        # if inner!=inner_max or outer!=0:
        #     outer+=1
        #     inner-=1
        #     count+=1
        # else:
        #     count+=1
        #     outer+=1
        #     inner-=1
        #     count+=1
        
       
    # print(count)

def spinning_rings(inner_max, outer_max):
    inner_step = inner_max
    outer_step = 1
    count = 0
    while True:
        if inner_step == 0:
            inner_step = inner_max

        inner_step -=1

        if outer_step == outer_max:
            outer_step = 0
        outer_step +=1
        
        if inner_step == outer_step:
            break
            
        count += 1
    return count

print(spinning_rings(2,3))

# print(3 % 1)
