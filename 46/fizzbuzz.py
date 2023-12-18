from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:


    if all(n % d == 0 for d in (3,5)):
        return 'Fizz Buzz'
    elif not n % 3:
        return 'Fizz'
    elif not n % 5:
        return 'Buzz'
    else:
        return num


