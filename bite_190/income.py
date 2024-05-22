import os
from pathlib import Path
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from collections import defaultdict

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/countries.xml", countries
    )


def get_income_distribution(xml=countries):
    """
    Read in the countries xml as stored in countries variable.
    Parse the XML
    Return a dict of:
      keys = incomes (wb:incomeLevel)
      values = list of country names (wb:name)
    """
    with open(xml) as f:
        contents = f.read()

    soup = BeautifulSoup(contents, features="lxml")
    income_distribution = defaultdict(list)

    for country in soup.find_all("wb:country"):
        income_level = country.find("wb:incomelevel").text
        country_name = country.find("wb:name").text
        if income_level not in income_distribution:
            income_distribution.setdefault(income_level, [])
        income_distribution[income_level].append(country_name)

    return income_distribution
