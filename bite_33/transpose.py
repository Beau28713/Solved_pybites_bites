def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if isinstance(data, dict):
        x = [
            tuple((date for date, post in data.items())),
            tuple((post for date, post in data.items())),
        ]

        return x

    y = [
        tuple((member.name for member in data)),
        tuple((member.since_days for member in data)),
        tuple((member.karma_points for member in data)),
        tuple((member.bitecoin_earned for member in data)),
    ]

    return y
