def fake_bin(x):
    y=""
    for i in x:
        if int(i)>=5:
            y+='1'
        else:
            y+='0'
    print(y)

fake_bin("45385593107843568")