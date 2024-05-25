"""
Model representing a club
"""

class Club:
    """
    Class representing a club
    """

    def __init__(self, abbreviation: str, full_name: str, club_id: int):
        self.abbreviation = abbreviation
        self.full_name = full_name
        self.club_id = club_id
