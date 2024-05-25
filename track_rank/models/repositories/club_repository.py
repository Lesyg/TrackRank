"""
Repository handling clubs
"""

import requests
from track_rank.endpoints import CLUBS
from track_rank.models.club import Club


# TODO improve so it return Club class
def get_clubs() -> list[Club]:
    """
    Get list of clubs
    """
    result = requests.get(CLUBS, timeout=10000)

    if result.json() is None:
        return []

    return [Club(club["Zkratka"], club["Name"], club["Id"]) for club in result.json()]
