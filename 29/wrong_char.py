ALPHANUMERIC = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def get_index_different_char(chars):
    check_list = []
    for char in chars:
        if str(char) in ALPHANUMERIC:
            check_list.append("+")
        else:
            check_list.append("-")

    number_of_alpha_char = check_list.count("+")
    number_of_non_alpha_char = check_list.count("-")

    if number_of_alpha_char == 1:
        for i in check_list:
            if i == "+":
                return check_list.index("+")

    if number_of_non_alpha_char == 1:
        for i in check_list:
            if i == "-":
                return check_list.index("-")
