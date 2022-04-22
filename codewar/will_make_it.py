
distance_to_pump=100
mpg=50
fuel_left=1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    """for given amount of ful will he make it to the destination

    Args:
        distance_to_pump (_type_): distance to next fuel pump
        mpg (_type_): miles per gallon of fuel
        fuel_left (_type_): gallon of fuel left

    Returns:
        _type_: _description_
    """
    #Happy Coding! ;)
    meter= mpg*fuel_left
    if meter>=distance_to_pump:
        return True
    else:
        return False
x=zero_fuel(distance_to_pump, mpg, fuel_left)
print(x)