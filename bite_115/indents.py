def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    mytable = text.maketrans("\t", "-")
    x = text.translate(mytable)

    left_strip = x.lstrip()
    text_len = len(text)
    left_len = len(left_strip)

    return text_len - left_len