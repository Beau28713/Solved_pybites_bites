"""In this Bite you are presented with a list of surnames, names, and countries. These 3 fields are in a multiline string, separated by a comma.

Code group_names_by_country, looping through the list, returning a collections.defaultdict where the keys are countries and the values are lists of concatenated names and surnames. The order of the keys (countries) and the value lists (names) does not matter.
"""

from collections import defaultdict
from pprint import pprint
from itertools import groupby

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    
    data_list = [x.split(',') for x in data.split()]

    group_itter = groupby(data_list[1:], lambda x: x[2])

    for key, group in group_itter:
        key_and_group = {key: list(group)}
        pprint(key_and_group)