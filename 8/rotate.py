def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    

    pos = abs(n)

    if pos > len(string):
        pos = len(string) % pos

    

    if n < 0:
        pos *= -1



    return string[pos:] + string[:pos]


    

