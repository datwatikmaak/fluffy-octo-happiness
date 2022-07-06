WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    even_rows = ""
    odd_rows = ""
    for i in range(size):
        if i % 2 == 0:
            even_rows += WHITE
            odd_rows += BLACK
        else:
            even_rows += BLACK
            odd_rows += WHITE

    for i in range(size):
        if i % 2 == 0:
            print(even_rows)
        else:
            print(odd_rows)
