"""
Model representing a result from a competition
"""

from datetime import date


class Result:
    """
    Class representing a result from a competition
    """

    def __init__(
        self,
        discipline: str,
        comp_date: date,
        placement: str | None,
        comp_id: int,
        result,
    ):
        self.discipline = discipline
        self.comp_date = comp_date
        self.comp_id = comp_id
        self.result = result

        if placement is None:
            self.placement = 0
        elif placement.isnumeric():
            self.placement = int(placement)
        elif placement.strip("=").isnumeric():
            self.placement = int(placement.strip("="))
        else:
            self.placement = 0

    def to_dict(self) -> dict:
        return {
            "Disciplina": self.discipline,
            "Datum": self.comp_date,
            "Umisteni": self.placement,
            "Id zavod": self.comp_id,
            "Vykon": self.result,
        }
