"""
File containing endpoints used for gathering data
"""

URL = "https://www.atletika.cz"
CLUB_MEMBERS = "https://is.atletika.cz/Members/MembersList/List/?club={club_id}&take=1000&memberType=RegisteredAthleteMember"
ATHLETE_RESULT = "https://is.atletika.cz/Members/MembersAthleteResultsList/List/?Ean={ean}&sezonaOd={year_from}&sezona={year_to}&take=500"
CLUBS = "https://is.atletika.cz/Clubs/ClubListItems/GetSelectList?searchText=&page=0&rows=500"
ATHLETE_EAN = "https://is.atletika.cz/Members/MembersList/List/?searchText={ean}&searchTextType=Ean&take=1000&memberType=RegisteredAthleteMember"
COMPETITION = "https://is.atletika.cz/Events/CalendarList/List/?season={season}&take=100000&skip=0"
