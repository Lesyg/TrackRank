import pytest
from models.competition import Competition
from models.repositories.competition_repository import get_competition_by_id


@pytest.mark.parametrize("comp_id", [[69922], [69923]])
def test_get_competition_by_id(comp_id):
    results = get_competition_by_id(comp_id)

    assert len(results) == 1
    assert isinstance(results[0], Competition)
    assert results[0].comp_id in comp_id
