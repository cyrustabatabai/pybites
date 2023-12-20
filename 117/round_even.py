import math
def round_even(number):
    
    """Takes a number and returns it rounded even"""


    if number - int(number) == 0.5:

        if int(number) % 2 == 0:
            return int(number)
        else:
            return int(number) + 1
    else:
        return round(number)

