from collections import Counter
def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """

    

    counts = Counter(c for c in sequence.upper() if c in 'AGCT')


    gc_count = counts['G'] + counts['C']


    total = sum(counts.values())

    return round(gc_count/total * 100,2)



