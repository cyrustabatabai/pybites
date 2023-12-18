INDENTS = 4


def print_hanging_indents(poem):


    lines = poem.split('\n')

    
    spaces = ' ' * 4
    new_lines = []
    prev = ''
    for line in lines:
        line = line.strip()

        if line:
            if not prev:
                new_lines.append(line)
            else:
                new_lines.append(f"{spaces}{line}")

        prev = line

    

    print('\n'.join(new_lines))
