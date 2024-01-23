def positive_divide(numerator, denominator):


    args = (numerator,denominator)

    if any(type(arg) not in (float,int) for arg in args):
        raise TypeError("Both arguments must be numbers")



    try:
        result = numerator/denominator
    except ZeroDivisionError:
        return 0
    else:
        if result <0: 
            raise ValueError

        return result
