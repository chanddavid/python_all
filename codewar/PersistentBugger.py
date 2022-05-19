def persistence(n):
    num = str(n)
    count = 0
    while len(num) > 1:
        result = 1
        for i in num:
            result=result* int(i)
        num = str(result)
        count += 1
    return count

x=persistence(999)
print(x)


