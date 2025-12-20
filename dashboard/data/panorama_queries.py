import streamlit as st
from db.connection import DuckDBConnection

@st.cache_data
def extremos_anual(indice, anio_inicio, anio_fin):
    con = DuckDBConnection()
    query = f"""
        SELECT
            anio,
            {indice} AS valor
        FROM dw.fact_extremos_anual
        WHERE anio BETWEEN ? AND ?
        ORDER BY anio
    """
    return con.execute(query, [anio_inicio, anio_fin]).df()

@st.cache_data
def extremos_estacional(indice, estacion, anio_inicio, anio_fin):
    con = DuckDBConnection()
    query = f"""
        SELECT
            anio,
            {indice} AS valor
        FROM dw.fact_extremos_estacional
        WHERE estacion = ?
          AND anio BETWEEN ? AND ?
        ORDER BY anio
    """
    return con.execute(query, [estacion, anio_inicio, anio_fin]).df()
