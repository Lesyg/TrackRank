import pytest
from models.athlete import Athlete
from models.repositories.athlete_repository import (get_athlete_by_ean,
                                                    get_athlete_results,
                                                    get_athletes_by_club)
from models.result import Result


@pytest.mark.parametrize(
    "club_id", [221, 609, 207, 314, 317, 802, 601, 1001, 1767, 1798, 1523]
)
def test_valid_club_ids(club_id):
    athletes = get_athletes_by_club(club_id)

    assert len(athletes) > 0
    assert isinstance(athletes[0], Athlete)


@pytest.mark.parametrize(
    "club_id",
    [
        0,
        1,
        10,
        20,
        55,
        60,
        99,
        100,
        101,
        220,
        608,
        200,
        310,
        318,
        800,
        600,
        1000,
        1794,
        2000,
    ],
)
def test_invalid_club_ids(club_id):
    athletes = get_athletes_by_club(club_id)

    assert len(athletes) == 0
    assert isinstance(athletes, list)


@pytest.mark.parametrize("ean", [10000007771, 10000007329, 10000004333, 10000004835])
def test_get_result_valid_ean(ean):
    results = get_athlete_results(ean)

    assert len(results) > 0
    assert isinstance(results[0], Result)


@pytest.mark.parametrize(
    "ean", [0, 1, 10, 20, 55, 60, 99, 100, 220, 608, 200, 310, 318, 800, 600]
)
def test_get_result_invalid_ean(ean):
    results = get_athlete_results(ean)

    assert len(results) == 0
    assert isinstance(results, list)


@pytest.mark.parametrize("ean", [10000007771, 10000007329, 10000004333, 10000004835])
def test_get_athlete_by_ean(ean):
    result = get_athlete_by_ean(ean)

    assert result is not None
    assert isinstance(result, Athlete)
    assert result.ean == ean
