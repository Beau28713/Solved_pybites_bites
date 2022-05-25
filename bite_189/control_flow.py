"""Complete filter_names that takes a list of names and returns a filtered 
list (or generator) of names using the following conditions:
names that start with IGNORE_CHAR are ignored,
names that have one or more digits are ignored,
if a name starts with QUIT_CHAR it inmediately exits the loop, so no more names 
are added/generated at this point (neither the QUIT_CHAR name),
return up till MAX_NAMES names max
"""
IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    name_list = []

    for name in names:
        if name.startswith(QUIT_CHAR):
            break
        elif name.startswith(IGNORE_CHAR):
            continue
        elif any(char.isdigit() for char in name):
            continue
        else:
            name_list.append(name)

        if len(name_list) >= MAX_NAMES:
            break
    
    return name_list