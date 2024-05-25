import pandas as pd
import plotly.graph_objects as go

# def create_stacked_bar_graph(data: pd.DataFrame) -> go.Figure:
#     athletes = data["Jmeno"] + " " + data["Prijmeni"]
#     competition_points = data["Zavodni body"]
#     bonus_points = data["Bonus"]
#
#     fig = go.Figure(
#         data=[
#             go.Bar(name="Zavodni body", x=athletes, y=competition_points),
#             go.Bar(name="Bonus", x=athletes, y=bonus_points),
#         ]
#     )
#
#     fig.update_layout(barmode="stack")
#
#     fig.update_layout(
#         title="Ziskane body podle bodovanych skupin",
#         xaxis_title="Atleti",
#         yaxis_title="Body",
#     )
#
#     return fig
