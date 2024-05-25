import datetime
from collections.abc import Iterable
from datetime import date

import pandas as pd
import plotly.graph_objects as go
import requests
from track_rank.endpoints import COMPETITION
from track_rank.models.athlete import Athlete
from track_rank.models.competition import Competition
from track_rank.models.repositories.athlete_repository import (
    get_athletes_by_club_list,
    get_athletes_by_ean_list,
)


class TrackRankModel:

    def __init__(self):
        pass

    def get_athletes_by_ean_list(self, list: list[int]) -> list[Athlete]:
        return get_athletes_by_ean_list(list)

    def get_athletes_by_club_list(self, list: Iterable[int]) -> list[Athlete]:
        return get_athletes_by_club_list(list)

    def create_stacked_bar_graph(self, data: pd.DataFrame) -> go.Figure:
        grouped = data.groupby(["Ean", "zavod_id", "zavod"]).sum().reset_index()

        categories = sorted(data["zavod_id"].unique())

        fig = go.Figure()

        for category in categories:
            category_data = grouped[grouped["zavod_id"] == category]
            fig.add_trace(
                go.Bar(
                    name=str(list(category_data["zavod"])[0]),
                    x=category_data["Jmeno"] + " " + category_data["Prijmeni"],
                    y=category_data["body"],
                )
            )

        # TODO add other categories

        fig.update_layout(barmode="stack")

        fig.update_layout(
            title="Ziskane body podle bodovanych skupin",
            xaxis_title="Atleti",
            yaxis_title="Body",
        )
        return fig

    def get_competitions(self, date_from: date, date_to: date) -> list[Competition]:
        competitions: list[Competition] = []
        for year in range(date_from.year, date_to.year + 1):
            result = requests.get(COMPETITION.format(season=year), timeout=10000)

            if result.status_code != 200:
                continue

            if result.json() is None:
                continue

            competitions.extend(
                [
                    Competition(
                        comp["Id"],
                        comp["Nazev"],
                        datetime.datetime.strptime(
                            comp["DtZahajeni"], "%Y-%m-%dT%H:%M:%S"
                        ).date(),
                    )
                    for comp in result.json()["data"]
                    if datetime.datetime.strptime(
                        comp["DtZahajeni"], "%Y-%m-%dT%H:%M:%S"
                    ).date()
                    >= date_from
                    and datetime.datetime.strptime(
                        comp["DtZahajeni"], "%Y-%m-%dT%H:%M:%S"
                    ).date()
                    <= date_to
                    and comp["Vysledky"] == "A"
                ]
            )

        return competitions
