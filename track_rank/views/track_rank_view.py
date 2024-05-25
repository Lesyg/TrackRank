"""
Class that is responsible for displaying components 
"""

import pandas as pd
import streamlit as st
from constants import (
    PROJECT_ABOUT_TEXT,
    PROJECT_NAME,
    PROJECT_README_URL,
    PROJECT_REPOSITORY_URL,
)
from track_rank.models.club import Club


class TrackRankView:
    """
    Displays streamlit components
    """

    def __init__(self) -> None:
        self.__configure()
        self.__initialize_session_state()

        st.sidebar.title("Track rank")

    def __configure(self) -> None:

        st.set_page_config(
            page_title=PROJECT_NAME,
            page_icon=":bar_chart:",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "Get Help": PROJECT_README_URL,
                "Report a bug": PROJECT_REPOSITORY_URL,
                "About": PROJECT_ABOUT_TEXT,
            },
        )

    def __initialize_session_state(self) -> None:
        """
        Initializes values in session state
        """

        if "list_of_eans" not in st.session_state:
            st.session_state.list_of_eans = {}

        if "table_of_points" not in st.session_state:
            st.session_state.table_of_points = pd.DataFrame([])
        if "comp_results" not in st.session_state:
            st.session_state.comp_results = pd.DataFrame([])

        if "selected_athletes" not in st.session_state:
            st.session_state.selected_athletes = []

        if "computed" not in st.session_state:
            st.session_state.computed = False

        if "athletes" not in st.session_state:
            st.session_state.athletes = set()

    def choose_collection(self) -> str | None:
        return st.sidebar.radio(
            label="**Vybrat atlety podle**",
            options=["ean", "club"],
            horizontal=True,
            index=0,
            format_func=lambda x: (
                "Unikátní identifikační číslo atleta"
                if x == "ean"
                else "Příslušnost zvoleného klubu"
            ),
        )

    def input_list(self, label: str) -> list[int]:
        with st.sidebar.form(key="ids_form" + label, clear_on_submit=True):
            st.text_input(label, key=label)

            st.form_submit_button(label="Přidat", on_click=self.__add_ids(label))

        return st.session_state.list_of_eans[label]

    def __add_ids(self, label: str):
        number = set(
            [
                int(num.strip())
                for num in st.session_state[label].split(",")
                if num.strip().isnumeric()
            ]
        )

        if label not in st.session_state.list_of_eans:
            st.session_state.list_of_eans[label] = number
        else:
            st.session_state.list_of_eans[label].update(number)

    def select_club(self, clubs: list[Club]) -> list[Club]:
        return st.sidebar.multiselect(
            label="Vyber oddíl",
            options=clubs,
            format_func=lambda x: x.full_name,
        )
