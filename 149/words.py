def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    numerics = []
    alphabets = []
   
    for word in words:

        # checking and inserting in respective container
        if word[0].isdigit():
            numerics.append(word)
        else:
            alphabets.append(word)

    # attaching lists post sort
    return sorted(alphabets, key=str.casefold) + sorted(numerics)
