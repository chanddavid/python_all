
moment="01:00 pm"
def moment_of_time_in_space(moment):
    output=[]
    time=0
    space=0
    for i in moment:
        if i.isdigit() and i!='0':
            time+=int(i)
        else:
            space+=1
    return [space > time, space == time, space < time]
x=moment_of_time_in_space(moment)
print(x)
