from models.repositories.club_repository import get_clubs
from models.club import Club


def test_get_clubs():
    clubs = get_clubs()

    assert isinstance(clubs, list)
    assert len(clubs) > 0
    assert isinstance(clubs[0], Club)
    assert clubs[0].club_id > 0
    assert clubs[0].full_name != ""
    assert clubs[0].abbreviation != ""
