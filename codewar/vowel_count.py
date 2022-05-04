

def get_count(sentence):

    # vowel='aeiou'
    count=0
    # for i in sentence:
    #     if i in vowel:
    #         count+=1
    # return count

    return len([count for i in sentence if i in "aeiou"])

x=get_count("abracadabra")
print(x)