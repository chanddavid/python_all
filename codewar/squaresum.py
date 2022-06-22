def square_sum(numbers):
    #your code here
    lst=0
    for i in numbers:
        x=i*i
        lst=lst+x
    return lst

square_sum([1,2])