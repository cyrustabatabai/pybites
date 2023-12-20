def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """


    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1


    return i if i < len(text) else 0

