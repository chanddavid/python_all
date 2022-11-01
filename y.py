test_list = [{'gfg': [1, 5, 6, 7], 'good': [9, 6, 2, 10],
              'CS': [4, 5, 6]},
             {'gfg': [5, 6, 7, 8], 'CS': [5, 7, 10]},
             {'gfg': [7, 5], 'best': [5, 7]}]
 
# printing original list

 
# Concatenate Similar Key values
# Using loop
res = dict()
for dict in test_list:

    for list in dict:
        print(list)
        if list in res:
            res[list] += (dict[list])
        else:
            res[list] = dict[list]
 
# printing result
# print("The concatenated dictionary : " + str(res))