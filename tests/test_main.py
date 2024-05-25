"""test views/main.py"""
from streamlit.testing.v1 import AppTest


def test_page_title_name():
    at = AppTest.from_file("track_rank/app.py").run()
    print(at)
    assert at.title[0].value == "Track rank"
    

