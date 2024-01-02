import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:


    if not args:
        return set()


    
    result = None
    for arg in args:
        try:
            arg = set(arg)
        except:
            continue
        else:

            if arg is not None and len(arg)> 0:
                if result is None:
                    result = arg
                else:
                    result &= arg



    return result if result is not None else set()

