


def to_nato(words):
    word=["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"]
    x=words.split(' ')
    lst=[]
    for i in x:
        for j in i:
            if j.isalpha():             
                for n,m in enumerate(word):
                    if j.upper() in m[0]:
                        lst.append(m)
            else:
                lst.append(j)
            
    result=" ".join(lst)               
    print(result)


to_nato('.d?d!')