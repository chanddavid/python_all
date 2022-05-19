def run_length_encoding(s):
    newlist = []
    count = 1
    char = s[0]
    for i in range(1,len(s)):
        if s[i] == char:
            count = count + 1
        else :
            newlist.append([char,count])
            char = s[i]
            count = 1
    newlist.append([char,count])
    print(newlist) 



run_length_encoding("abcbbb baa")