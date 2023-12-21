WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

    even_row = ''.join(' ' if i % 2 == 0 else '#' for i in range(size))
    odd_row = ''.join('#' if i % 2 == 0 else ' ' for i in range(size))


    rows = [even_row if i % 2 == 0 else odd_row for i in range(size)]


    print('\n'.join(rows))



