import pandas as pd


def clean_and_transform_data(df):
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce", utc=True)
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month
    df.dropna(subset=["date_added"], inplace=True)

    return df
