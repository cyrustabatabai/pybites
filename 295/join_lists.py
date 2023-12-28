from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    
    if not lst_of_lst:
        return

    result = []
    for lst in lst_of_lst:
        result.extend(lst)
        result.append(sep)
    if result:
        result.pop()
    return result

