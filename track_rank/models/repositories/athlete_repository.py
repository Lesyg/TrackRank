"""
Repository handling athletes
"""

from collections.abc import Iterable
from datetime import datetime

import requests
from endpoints import ATHLETE_EAN, ATHLETE_RESULT, CLUB_MEMBERS
from models.athlete import Athlete
from models.result import Result


def get_athletes_by_club(club_id: int) -> list[Athlete]:
    """Get list of athletes that belong to club"""
    athletes = requests.get(CLUB_MEMBERS.format(club_id=club_id), timeout=10000)

    if athletes.status_code != 200:
        return []

    data = athletes.json()["data"]

    if not isinstance(data, list):
        return []

    print(data)
    return [
        Athlete(
            at["Jmeno"],
            at["Prijmeni"],
            at["Ean"],
            # repre_from=datetime.strptime(at["RepreClenOd"], "%Y-%m-%dT%H:%M:%S"),
            # repre_to=datetime.strptime(at["RepreClenDo"], "%Y-%m-%dT%H:%M:%S"),
        )
        for at in data
    ]


def get_athlete_by_ean(ean: int) -> Athlete | None:
    """
    Get an athlete using ean
    """
    athlete = requests.get(ATHLETE_EAN.format(ean=ean), timeout=10000)

    if athlete.status_code != 200:
        return None

    data = athlete.json()["data"]

    if not isinstance(data, list) or len(data) == 0:
        return None

    repre_from = data[0]["RepreClenOd"]
    repre_to = data[0]["RepreClenDo"]

    if repre_from is not None:
        repre_from = datetime.strptime(repre_from, "%Y-%m-%dT%H:%M:%S")

    if repre_to is not None:
        repre_to = datetime.strptime(repre_to, "%Y-%m-%dT%H:%M:%S")

    return Athlete(
        data[0]["Jmeno"],
        data[0]["Prijmeni"],
        data[0]["Ean"],
        repre_from=repre_from,
        repre_to=repre_to,
    )


def get_athlete_results(
    ean: int, year_from: str = "2024", year_to: str = "2024"
) -> list[Result]:
    """
    Get results of an athlete within the timeframe
    """
    results = requests.get(
        ATHLETE_RESULT.format(ean=ean, year_from=year_from, year_to=year_to),
        timeout=10000,
    )

    if results.status_code != 200:
        return []

    data = results.json()["data"]

    if not isinstance(data, list):
        return []

    return [
        Result(
            at["IdDiscipline"],
            datetime.strptime(at["From"], "%Y-%m-%dT%H:%M:%S").date(),
            at["Order"],
            int(at["IdEvent"]),
            at["Result"],
        )
        for at in data
    ]


def get_athletes_by_ean_list(eans: list[int]) -> list[Athlete]:
    """
    Get a list of athletes based on eans
    """
    athletes: list[Athlete] = []
    for ean in eans:
        athlete = get_athlete_by_ean(ean)
        if athlete:
            athletes.append(athlete)

    return athletes


def get_athletes_by_club_list(club_ids: Iterable[int]) -> list[Athlete]:
    """Get list of athletes that belong to the list"""

    athletes: list[Athlete] = []
    for club_id in club_ids:
        athletes.extend(get_athletes_by_club(club_id))

    return athletes
