import math
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """

    f = math.ceil if up else math.floor


    return [int(f(value)) for value in transactions]
    



