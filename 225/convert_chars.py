PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""

    result = []

    for c in text:
        if c.lower() in PYBITES:
            result.append(c.swapcase())
        else:
            result.append(c)


    return ''.join(result)
