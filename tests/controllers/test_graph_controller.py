import pandas as pd
import plotly.graph_objects as go
from controllers.graph_controller import create_stacked_bar_graph


def test_create_stacked_bar_graph():
    data = pd.DataFrame(
        {
            "Jmeno": ["John", "Jane", "Doe"],
            "Prijmeni": ["Doe", "Smith", "Johnson"],
            "Soucet bodu": [10, 15, 20],
        }
    )

    fig = create_stacked_bar_graph(data)

    assert isinstance(fig, go.Figure)

    # Check the figure data
    assert len(fig.data) == 1
    assert fig.data[0].type == "bar"
    assert fig.data[0].name == "Zavodni body"
    assert fig.data[0].x.tolist() == [
        "John Doe",
        "Jane Smith",
        "Doe Johnson",
    ]
    assert fig.data[0].y.tolist() == [10, 15, 20]

    # Check the layout
    assert fig.layout.barmode == "stack"
    assert fig.layout.title.text == "Ziskane body podle bodovanych skupin"
    assert fig.layout.xaxis.title.text == "Atleti"
    assert fig.layout.yaxis.title.text == "Body"
