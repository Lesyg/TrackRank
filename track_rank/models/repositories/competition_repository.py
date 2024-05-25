"""
Repository handling competitions
"""

from datetime import datetime

import requests
from endpoints import COMPETITION
from models.competition import Competition


def get_competition_by_id(
    comp_id: list[int], season: str = "2024"
) -> list[Competition]:
    """
    Get results of an athlete within the timeframe
    """
    results = requests.get(
        COMPETITION.format(season=season),
        timeout=10000,
    )

    if results.status_code != 200:
        return []

    data = results.json()["data"]

    if not isinstance(data, list):
        return []

    return [
        Competition(
            at["Id"],
            at["Nazev"],
            datetime.strptime(at["DtZahajeni"], "%Y-%m-%dT%H:%M:%S").date(),
        )
        for at in data
        if at["Id"] in comp_id
    ]
