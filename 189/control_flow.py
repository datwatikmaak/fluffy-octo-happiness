IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    list_of_names = []
    for name in names:
        if name.startswith("b"):
            continue
        if any(char.isdigit() for char in name):
            continue
        if name.startswith("q"):
            break
        else:
            list_of_names.append(name)

    return list_of_names[:5]
