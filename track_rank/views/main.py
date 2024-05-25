import datetime

import pandas as pd
import streamlit as st
from track_rank.controllers.data_controller import (
    collect_results,
    merge_points_results,
    merge_points_results_all,
    to_excel,
)
from track_rank.models.competition import Competition
from track_rank.models.repositories.club_repository import get_clubs
from track_rank.models.track_rank_model import TrackRankModel
from track_rank.views.track_rank_view import TrackRankView


def display_competition(comp_list: list[Competition]) -> pd.DataFrame:
    st.write("Závody")
    comps_df = pd.DataFrame([comp.to_dict() for comp in comp_list])
    return st.data_editor(comps_df, use_container_width=True, num_rows="dynamic")


def add_points():
    if (
        st.session_state["umisteni od"]
        and st.session_state["umisteni do"]
        and st.session_state["body"]
        and st.session_state["zavod"]
    ):
        for place in range(
            st.session_state["umisteni od"], st.session_state["umisteni do"] + 1
        ):

            new_row = pd.DataFrame(
                {
                    "umisteni": [place],
                    "body": [st.session_state["body"]],
                    "zavod": [
                        st.session_state["zavod"].Nazev
                        + " "
                        + str(st.session_state["zavod"].Datum)
                    ],
                    "zavod_id": [st.session_state["zavod"].id],
                }
            )
            st.session_state.table_of_points = pd.concat(
                [st.session_state.table_of_points, new_row], ignore_index=True
            )


def fill_points(comps: pd.DataFrame):
    with st.sidebar.form("**Vyplň příslušné ohodnoceni**", clear_on_submit=True):
        st.number_input("umisteni od", key="umisteni od", step=1)
        st.number_input("umisteni do", key="umisteni do", step=1)
        st.number_input("body", key="body", step=1)
        st.selectbox(
            "zavod",
            options=comps.itertuples(index=False),
            key="zavod",
            format_func=lambda x: x[1] + " " + str(x[2]),
        )

        st.form_submit_button("Přidat", on_click=add_points)


def select_athletes(athletes: pd.DataFrame) -> list[int]:
    selected = st.multiselect(
        label="",
        options=athletes.itertuples(index=False),
        format_func=lambda x: x[1] + " " + x[1],
    )

    st.session_state.selected_athletes = list(map(lambda x: x["Ean"], selected))

    return st.session_state.selected_athletes


def main():
    """
    Main method to run view
    """

    view = TrackRankView()
    model = TrackRankModel()

    cl1, cl2 = st.sidebar.columns(2)
    filter_by_date = cl1.toggle("Filtrovat podle datumu")
    ignore_ms = cl2.toggle("Ignorovat starty mimo soutěž")

    today = datetime.datetime.now()
    date_from = datetime.date(today.year, 1, 1)
    date_to = datetime.date(today.year, 12, 31)

    if filter_by_date:
        col1, col2 = st.sidebar.columns(2)
        date_from = col1.date_input(
            label="Od",
            value=today,
            format="DD.MM.YYYY",
        )

        date_to = col2.date_input(
            label="Do",
            value=today,
            format="DD.MM.YYYY",
        )

        if date_from > date_to:
            st.sidebar.error("Do musí nastat až po od")

    collection_type = view.choose_collection()

    if collection_type == "ean":
        id_list = view.input_list("Seznam identifikačních čisel atletů")
        with st.spinner("Hledani atletů"):
            st.session_state.athletes.update(model.get_athletes_by_ean_list(id_list))
    else:
        clubs = get_clubs()
        id_list = view.select_club(clubs)
        with st.spinner("Hledani atletů"):
            st.session_state.athletes.update(
                model.get_athletes_by_club_list(map(lambda x: x.club_id, id_list))
            )

    if st.session_state.athletes:

        athlete_df = pd.DataFrame(
            [athlete.to_dict() for athlete in st.session_state.athletes]
        )
        print(st.session_state.athletes)
        athlete_df["Bonus"] = 0
        st.title("Vybraní atleti")
        athlete_df = st.data_editor(
            athlete_df, num_rows="dynamic", use_container_width=True
        )

        # comp_list = view.input_list("Seznam identifikačních čísel závodů")

        comp_list = st.sidebar.multiselect(
            label="Zavody",
            options=model.get_competitions(date_from, date_to),
            format_func=lambda x: x.name,
        )

        if comp_list:

            comps = display_competition(comp_list)

            fill_points(comps)

            if not st.session_state.table_of_points.empty:
                st.session_state.table_of_points = st.data_editor(
                    st.session_state.table_of_points,
                    use_container_width=True,
                    num_rows="dynamic",
                )

                if (
                    st.button("Načíst výsledky")
                    or not st.session_state.comp_results.empty
                ):
                    st.write("Vysledky")
                    with st.spinner("Hledani vysledku"):
                        st.session_state.comp_results = collect_results(
                            athlete_df, comps
                        )
                        st.session_state.comp_results = st.data_editor(
                            st.session_state.comp_results,
                            use_container_width=True,
                            num_rows="dynamic",
                        )

                    if st.button("Spocitej") or st.session_state.computed:
                        result_df = merge_points_results(
                            athlete_df,
                            st.session_state.comp_results,
                            st.session_state.table_of_points,
                        )

                        full_result = merge_points_results_all(
                            athlete_df,
                            st.session_state.comp_results,
                            st.session_state.table_of_points,
                        )
                        st.title("**Soucet bodu**")

                        if st.toggle("Pouze bodující"):
                            full_result = full_result[full_result["Body celkem"] != 0]

                        st.data_editor(
                            full_result.sort_values(by="Body celkem", ascending=False),
                            use_container_width=True,
                        )

                        st.session_state.computed = True

                        left, right = st.columns(2)
                        left.download_button(
                            "Stahnout data csv",
                            full_result.to_csv(index=False).encode("utf-8"),
                            file_name="data.csv",
                        )
                        right.download_button(
                            label="Stahnout data excel",
                            data=to_excel(full_result),
                            file_name="data.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        )

                        with st.expander("**Vyber atlety k porovnani**"):
                            st.session_state.selected_athletes = select_athletes(
                                result_df
                            )

                        if st.session_state.selected_athletes:
                            st.plotly_chart(
                                model.create_stacked_bar_graph(
                                    result_df[
                                        result_df["Ean"].isin(
                                            st.session_state.selected_athletes
                                        )
                                    ]
                                ),
                                use_container_width=True,
                            )
                        else:
                            st.plotly_chart(
                                model.create_stacked_bar_graph(
                                    result_df[result_df["body"] != 0]
                                ),
                                use_container_width=True,
                            )
