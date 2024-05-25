# from views.configuration import configure, initialize_session_state
from streamlit.testing.v1 import AppTest
from flexmock import flexmock
import streamlit as st
from views.configuration import initialize_session_state
import pandas as pd


def test_configure():
    # import streamlit as st
    # import pandas as pd

    app = AppTest.from_file("track_rank/app.py")


# def test_initialize_session_state():

# app = AppTest.from_file("track_rank/app.py")


# print(app.session_state)
# assert "list_of_eans" in app.session_state
# assert isinstance(app.session_state.list_of_eans, dict)
# assert len(app.session_state.list_of_eans) == 0
#
# assert "table_of_points" in app.session_state
# assert "comp_results" in app.session_state
# assert "selected_athletes" in app.session_state
# assert "computed" in app.session_state


def test_initialize_session_state():
    # Mock the st.session_state with flexmock
    mock_session_state = flexmock(st.session_state)
    mock_session_state.should_receive("__setitem__").and_return()
    mock_session_state.should_receive("__getitem__").and_return({})

    initialize_session_state()

    # assert "list_of_eans" in st.session_state
    # assert st.session_state.list_of_eans == {}
    #
    # assert "table_of_points" in st.session_state
    # # assert isinstance(st.session_state.table_of_points, pd.DataFrame)
    # assert st.session_state.table_of_points.columns.tolist() == [
    #     "umisteni",
    #     "body",
    #     "zavod",
    # ]
    #
    # assert "comp_results" in st.session_state
    # # assert isinstance(st.session_state.comp_results, pd.DataFrame)
    # assert st.session_state.comp_results.empty
    #
    # assert "selected_athletes" in st.session_state
    # assert st.session_state.selected_athletes == []
    #
    # assert "computed" in st.session_state
    # assert st.session_state.computed is False
