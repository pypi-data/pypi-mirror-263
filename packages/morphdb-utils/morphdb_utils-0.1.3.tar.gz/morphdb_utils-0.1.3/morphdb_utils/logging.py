import pandas as pd


def render(df: pd.DataFrame):
    print(convert_dataframe_to_render_format(df))


def convert_dataframe_to_render_format(df: pd.DataFrame):
    data = df.to_dict(orient="records")
    headers = list(df.columns)
    return {"records": data, "headers": headers}