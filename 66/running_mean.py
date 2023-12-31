from itertools import accumulate

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    return (round(s/n,2) for n,s in enumerate(accumulate(sequence),1))
