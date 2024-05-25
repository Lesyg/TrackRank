"""
Model that represent a competition
"""

from datetime import date


class Competition:
    """
    Class representing a competition
    """

    def __init__(self, comp_id: int, name: str, date: date):
        self.comp_id = comp_id
        self.name = name
        self.date = date

    def to_dict(self) -> dict:
        return {"id": self.comp_id, "Nazev": self.name, "Datum": self.date}

    def __hash__(self) -> int:
        return self.comp_id

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Competition):
            return False

        if not value.comp_id == self.comp_id:
            return False

        if not value.name == self.name:
            return False

        if not value.date == self.date:
            return False

        return True
