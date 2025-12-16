import pandas as pd
from src.config.settings import DATA_METEO, DATA_ENSO

def extract_lp_raw():
    df_temp = pd.read_excel(
        f"{DATA_METEO}/temp-la-plata-aero.xlsx",
        skiprows=3,
        names=["fecha", "t_max", "t_min", "t_media"]
    )

    df_pp = pd.read_excel(
        f"{DATA_METEO}/pp-la-plata-aero.xlsx",
        skiprows=3,
        names=["fecha", "pp"]
    )

    return pd.merge(df_temp, df_pp, on="fecha")

def extract_station_hourly(file):
    return pd.read_excel(
        f"{DATA_METEO}/{file}",
        skiprows=5,
        names=["fecha", "hora", "temp", "pp"]
    )
