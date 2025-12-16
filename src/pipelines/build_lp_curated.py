from src.etl.extract import extract_lp_raw, extract_station_hourly
from src.utils.prepare import filtrar_periodo
from src.utils.breakpoints import aplicar_tests, construir_periodos
from src.utils.imputation import imputar_serie

def main():
    
    df_lp = extract_lp_raw()
    df_aeroparque = extract_station_hourly("AEROPARQUE_AERO.xlsx")
    df_ezeiza = extract_station_hourly("EZEIZA_AERO.xlsx")
    df_obs_bsas = extract_station_hourly("BUENOS_AIRES_OBSERVATORIO.xlsx")
    df_punta_indio = extract_station_hourly("PUNTA_INDIO_B.A..xlsx")

    df_lp = filtrar_periodo(df_lp)
    df_aeroparque = filtrar_periodo(df_aeroparque)
    df_ezeiza = filtrar_periodo(df_ezeiza)
    df_obs_bsas = filtrar_periodo(df_obs_bsas)
    df_punta_indio = filtrar_periodo(df_punta_indio)

    

    # análisis de quiebres (una vez)
    quiebres = aplicar_tests(df_lp["t_media"].dropna())

    periodos = construir_periodos(
        quiebres,
        df_lp["fecha"].min(),
        df_lp["fecha"].max()
    )

    # imputación
    df_lp["t_media"] = imputar_serie(
        df_lp["t_media"],
        periodos,
        X=df_lp[["t_min", "t_max"]]
    )

    df_lp.to_csv("data/curated/lp_diario.csv", index=False)

if __name__ == "__main__":
    main()
