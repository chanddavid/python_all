def find_children(dancing_brigade):
    # your code here
    # print(''.join(sorted(dancing_brigade,key=lambda L: (L.lower(), L))))
    print(''.join(sorted(sorted(dancing_brigade),key=str.lower)))


find_children("CbcBcbaA")


#  key=str.lower
