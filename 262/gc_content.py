def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    a = sequence.lower().count("a")
    c = sequence.lower().count("c")
    g = sequence.lower().count("g")
    t = sequence.lower().count("t")

    return round(((c + g) / (a + c + g + t)) * 100, 2)
