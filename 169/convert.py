def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """

    needed_parts = ['cm','in']

    if type(value) not in (float,int):
        raise TypeError


    if not any(part == fmt.lower() for part in needed_parts):
        raise ValueError



    if fmt.lower() == 'in':
        return round(value * 1/2.54,4)
    else:
        return round(value * 2.54,4)



    
