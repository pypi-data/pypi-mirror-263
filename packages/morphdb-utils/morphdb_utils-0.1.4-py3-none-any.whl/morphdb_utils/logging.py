import pandas as pd


def render(data):
    if isinstance(data, pd.DataFrame):
        print(convert_dataframe_to_render_format(data))
    else:
        print(data)


def convert_dataframe_to_render_format(df: pd.DataFrame):
    data = df.to_dict(orient="records")
    headers = list(df.columns)
    return {"records": data, "headers": headers}