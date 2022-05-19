def reverse_alternate(string):
    words=string.split()
    words[1::2]=[word[::-1] for word in words[1::2]]
    return ' '.join(words)

reverse_alternate("Reverse this string, please!")