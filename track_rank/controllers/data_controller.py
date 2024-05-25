"""
Controller responsible for dealing with data processing
"""

import pandas as pd
import streamlit as st

from io import BytesIO
from track_rank.models.repositories.athlete_repository import get_athlete_results


# @st.cache_data
# def merge_points_resutls(
#     athlete_df: pd.DataFrame, comp_results, table_of_points
# ) -> pd.DataFrame:
#     merged_df = pd.merge(
#         comp_results,
#         table_of_points,
#         how="left",
#         left_on=["zavod_id", "umisteni"],
#         right_on=["zavod_id", "umisteni"],
#     )
#
#     merged_df.drop("umisteni", axis=1, inplace=True)
#
#     collected_points_df = merged_df.groupby("Ean")["body"].sum().reset_index()
#     collected_points_df.rename(columns={"body": "Zavodni body"}, inplace=True)
#
#     result_df = pd.merge(athlete_df, collected_points_df, how="left", on="Ean")
#
#     result_df["Zavodni body"].fillna(0, inplace=True)
#     result_df["Body celkem"] = result_df["Zavodni body"] + result_df["Bonus"]
#     return result_df


@st.cache_data
def merge_points_results(
    athlete_df: pd.DataFrame, comp_results, table_of_points
) -> pd.DataFrame:
    merged_df = pd.merge(
        comp_results,
        table_of_points,
        how="left",
        left_on=["zavod_id", "umisteni"],
        right_on=["zavod_id", "umisteni"],
    )

    # merged_df.drop("umisteni", axis=1, inplace=True)

    # collected_points_df = merged_df.groupby("Ean")["body"].sum().reset_index()
    # collected_points_df.rename(columns={"body": "Zavodni body"}, inplace=True)
    #
    result_df = pd.merge(athlete_df, merged_df, how="outer", on="Ean")
    result_df = result_df.dropna()

    result_df = (
        result_df.groupby(["zavod_id", "Ean", "zavod"])["body"].sum().reset_index()
    )
    result_df = pd.merge(athlete_df, result_df, how="outer", on="Ean").dropna()

    #
    # result_df["Zavodni body"].fillna(0, inplace=True)
    # result_df["Body celkem"] = result_df["Zavodni body"] + result_df["Bonus"]
    return result_df


@st.cache_data
def merge_points_results_all(
    athlete_df: pd.DataFrame, comp_results, table_of_points
) -> pd.DataFrame:
    merged_df = pd.merge(
        comp_results,
        table_of_points,
        how="left",
        left_on=["zavod_id", "umisteni"],
        right_on=["zavod_id", "umisteni"],
    )

    merged_df.drop("umisteni", axis=1, inplace=True)

    collected_points_df = merged_df.groupby("Ean")["body"].sum().reset_index()
    collected_points_df.rename(columns={"body": "Zavodni body"}, inplace=True)
    result_df = pd.merge(athlete_df, collected_points_df, how="left", on="Ean")

    result_df["Zavodni body"].fillna(0, inplace=True)
    result_df["Body celkem"] = result_df["Zavodni body"] + result_df["Bonus"]
    return result_df


@st.cache_data
def collect_results(athletes: pd.DataFrame, comp_list: pd.DataFrame) -> pd.DataFrame:
    res_list = pd.DataFrame([])
    for ean in athletes["Ean"]:
        rf_list = get_athlete_results(ean)
        res_list = pd.concat(
            [
                res_list,
                pd.DataFrame(
                    [
                        (
                            {
                                "Disciplina": r.discipline,
                                "Datum": r.comp_date,
                                "umisteni": r.placement,
                                "zavod_id": r.comp_id,
                                "Vykon": r.result,
                                "Ean": ean,
                            }
                        )
                        for r in filter(
                            lambda x: x.comp_id
                            in comp_list["id"].astype(int).to_list(),
                            rf_list,
                        )
                    ]
                ),
            ]
        )

    return res_list


def to_excel(df: pd.DataFrame):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")

    processed_data = output.getvalue()

    return processed_data
