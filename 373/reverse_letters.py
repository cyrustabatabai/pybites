def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""

    
    stack = []
    result = [None] * len(string)


    for i,c in enumerate(string):
        if c.isalpha():
            stack.append(c)
        else:
            result[i] = c
    

    

    for i,value in enumerate(result):
        if not value:
            result[i] = stack.pop()



    return ''.join(result)


if __name__ == "__main__":
    reverse_letters()
