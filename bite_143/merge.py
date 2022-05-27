from collections import ChainMap

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if isinstance(name, str):
        name = name.lower()
        combined = ChainMap(group1, group2, group3)
        rev = list(combined.maps[::-1])
        print(rev)

        if name in combined:
            for ele in rev:
                if name in ele:
                    return ele.get(name)
        else:
            return NOT_FOUND
    
    else:
        return NOT_FOUND