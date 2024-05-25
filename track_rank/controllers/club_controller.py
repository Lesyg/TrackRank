"""
Controller for clubs
"""

import requests
from bs4 import BeautifulSoup


def get_clubs():
    """
    Return list of clubs
    """

    result = requests.get(
        "https://online.atletika.cz/clenska-sekce/oddily/adresar-oddilu/", timeout=10000
    )

    soup = BeautifulSoup(result.text, "html.parser")

    # print(soup.find_all("tbody"))
    if soup.tbody is None:
        return []

    tr = soup.tbody.find_all("tr")

    soup = BeautifulSoup("\n".join([str(x) for x in tr]), "html.parser")

    for t in tr:
        print(t.find_next("td").find_next("td").text)
