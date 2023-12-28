from collections import Counter
def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    

    counts = Counter(numbers)
    
    values = counts.values()
    min_count,max_count = min(values),max(values)

    minor,major = [number for count in (min_count,max_count) for number,c in counts.items() if c == count]










    return major, minor
