import streamlit as st

st.set_page_config(
    page_title="Dashboard Climático",
    layout="wide"
)

st.title("Dashboard Climático")
st.markdown("""
Este dashboard utiliza un modelo dimensional
y DuckDB como base analítica.
""")

st.info("Usá el menú lateral para navegar entre páginas.")
