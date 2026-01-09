import pandas as pd

def convert_df(df_pm25):
    df = df_pm25.copy()

    formated = (
        df
        .set_index(("datetime", ""))
        .stack(["Miejscowość", "Kod stacji"])
        .reset_index()
    )

    formated.columns = ["datetime", "Miejscowość", "Kod stacji", "PM25"]
    return formated


def calc_monthly_means(formated):
    df = formated.copy()
    df["PM25"] = pd.to_numeric(df["PM25"], errors="coerce")

    return (
        df.groupby([
            df["datetime"].dt.year.rename("Rok"),
            df["datetime"].dt.month.rename("Miesiąc"),
            "Miejscowość",
            "Kod stacji"
        ])["PM25"].mean().reset_index(name="Mean PM25")
    )