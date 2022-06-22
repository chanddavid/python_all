def nb_dig(n, d):
    # your code
    count=0
    s=str(d)
    for i in range(n+1):
        num=i*i
        count+=str(num).count(s)
    return count