def get_profile(name: str, age: int, *args, **kwargs) -> dict:
    if not isinstance(age, int):
        raise ValueError

    if len(args) >= 6:
        raise ValueError

    my_dict = {}

    if args and kwargs:
        my_dict.update(
            {"name": name, "age": age, "sports": sorted([*args]), "awards": {**kwargs}}
        )

    if args:
        my_dict.update({"name": name, "age": age, "sports": sorted([*args])})
        return my_dict

    if kwargs:
        my_dict.update({"name": name, "age": age, "awards": {**kwargs}})

    my_dict.update({"name": name, "age": age})

    return my_dict
