import os
import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    dedented = textwrap.dedent(poem).splitlines()

    indexes = list(range(len(dedented) + 1))
    sentences = list(dedented)

    text = ""
    get_empty = []
    first_line = []
    for i, s in zip(indexes, sentences):
        if s == "":
            get_empty.append(i)
            first_line.append(i + 1)

        if i in get_empty:
            text += s
        elif i in first_line:
            text += s + '\n'
        else:
            text += (" " * INDENTS) + s + '\n'

    print(text)
