
def is_narcissistic(i):
    num = str(i)
    power = len(num)
    sum = 0
    for number in num:
        sum += int(number) ** power
    if sum == i:
        return True
    return False

x=is_narcissistic(1634)
print(x)

