import streamlit as st
import plotly.express as px

def line_chart(df, x, y, title, y_label):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        labels={
            x: "Año",
            y: y_label
        },
        title=title
    )
    fig.update_layout(template="simple_white")
    return fig
