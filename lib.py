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


