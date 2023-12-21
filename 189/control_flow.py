IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):

    
    names_returned = 0
    for name in names:
        if name[0] == QUIT_CHAR:
            break
        if name[0] == IGNORE_CHAR:
            continue


        if sum(str(digit) in name for digit in range(0,10)) >= 1:
            continue

        yield name
        names_returned += 1
        if names_returned == MAX_NAMES:
            break




