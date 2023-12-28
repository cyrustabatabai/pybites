def round_to_next(number: int, multiple: int):

    return multiple * (number//multiple + (1 if number% multiple else 0))
