def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    common_lang = set(programmers[list(programmers.keys())[0]])
    for programmer in programmers:
        common_lang = common_lang & set(programmers[programmer])
    return common_lang
