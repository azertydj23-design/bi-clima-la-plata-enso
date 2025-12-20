import streamlit as st

from db.connection import DuckDBConnection
from dashboard.data.clima_queries import get_registros_por_anio
from dashboard.components.charts import line_chart_anio

st.title("Prueba de arquitectura")

df = get_registros_por_anio()

st.write("Vista previa de datos")
st.dataframe(df.head())

line_chart_anio(
    df,
    x_col="anio",
    y_col="registros",
    title="Cantidad de registros por año"
)
