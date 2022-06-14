


def func():
    tuples=(['har','ram'],['sam'])
    x=tuples[0]
    x+=['alex']

    try:
        tuples[0]+=['james']
        
    except TypeError:
        print("error")

    print(tuples)
    # x=1
    # y=[2]
    # x,=y
    # print(x)
 
func()
