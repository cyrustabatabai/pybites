import math
def is_armstrong(n: int) -> bool:

    num_digits = int(math.log(n,10)) + 1


    original = n
    s = 0

    while n:
        s += (n % 10)**num_digits
        if s > original:
            break

        n //= 10


    return s == original







