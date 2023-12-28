from typing import List, TypeVar
import math
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError()


    result = []
    for number in numbers:
        multiplier = 1

        if number == 0:
            result.append(number)
        else:
            if number < 0:
                multiplier = -1
                number = abs(number)




            num_digits = int(math.log(int(number),10)) + 1


            mult = 10 ** (n - num_digits )

            result.append(int(mult * number) * multiplier)

    return result





