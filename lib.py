import math
def cashback(monthly_expenses): #объявление + указание параметра
    """
    >>> cashback(10_000)
    300.0
    """
    percent = 3
    result = percent * monthly_expenses / 100
    return result #возврат значения

def bmi(mass, growth):
    """
    >>> bmi(75,1.83) #doctest: +ELLIPSIS
    22.39...
    """
    result = mass / (growth**2)
    return result

def distance_calculation(volume_fuel,expense_fuel):
    """
    >>> distance_calculation(20,10)
    200.0
    """
    result = volume_fuel * 100 / expense_fuel
    return result

def perimeter_of_the_room(width_of_the_room,length_of_the_room):
    """
    >>> perimeter_of_the_room(3,5)
    16
    """
    perimeter_of_the_room = float(width_of_the_room + length_of_the_room) * 2
    return perimeter_of_the_room
