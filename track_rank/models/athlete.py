"""
Model representing an athlete
"""

from datetime import datetime, date


class Athlete:
    """
    Class representing an athlete
    """

    def __init__(
        self,
        name: str,
        surname: str,
        ean: int,
        national_repre: bool = False,
        repre_from: date | None = None,
        repre_to: date | None = None,
    ):
        print(national_repre)
        print(repre_from)
        print(repre_to)
        self.name = name
        self.surname = surname
        self.ean = ean
        if national_repre:
            self.national_repre = national_repre
        elif repre_from and repre_to is None:
            self.national_repre = True
        elif repre_from and repre_to is not None and repre_to > datetime.now():
            self.national_repre = True
        else:
            self.national_repre = False

    def to_dict(self):
        return {
            "Jmeno": self.name,
            "Prijmeni": self.surname,
            "Ean": self.ean,
            "Repre": self.national_repre,
        }

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Athlete):
            return False

        if value.name != self.name:
            return False

        if value.name != self.name:
            return False
        if value.ean != self.ean:
            return False

        return True

    def __hash__(self) -> int:
        return self.ean

    def __str__(self) -> str:
        return f"Athlete({self.name} {self.surname}, {self.ean}, {self.national_repre})"

    def __repr__(self) -> str:
        return f"Athlete(name='{self.name}', surname='{self.surname}', ean='{self.ean}', national_repre='{self.national_repre}')"
