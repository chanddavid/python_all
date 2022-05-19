def duplicate_count(text):
    occured=[]
    found=[]
    count=0
    for letter in text:
        if letter.lower() not in occured:
            occured.append(letter.lower())
        else:
            if letter.lower() not in found:
                count+=1
                found.append(letter.lower())
    return count

x=duplicate_count('abcde')
print(x)