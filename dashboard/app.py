import streamlit as st

st.set_page_config(
    page_title="Dashboard Climático – ENSO",
    layout="wide"
)

st.title("🌍 Dashboard Climático – Análisis ENSO")

st.markdown("""
### 📌 Introducción

Este dashboard presenta un **análisis exploratorio y comparativo del fenómeno ENSO
(El Niño–Oscilación del Sur)**, integrando información oceánica y atmosférica
a través de distintos **índices climáticos reconocidos**.

El objetivo principal es **caracterizar el comportamiento temporal, la intensidad
y la variabilidad del ENSO**, así como su relación con el **panorama climático general**.
""")

st.markdown("""
---

### 🌊 ENSO: Fenómeno Analizado

El ENSO es un fenómeno climático de escala global que alterna entre tres fases:

- **El Niño**
- **La Niña**
- **Condición Neutra**

Estas fases se definen a partir de anomalías en la temperatura superficial del mar
y en la circulación atmosférica del Pacífico ecuatorial.
""")

st.markdown("""
---

### 📊 Índices ENSO y Variables Analizadas

Para describir el fenómeno se emplean múltiples índices, cada uno con una
interpretación física específica:

- **ONI**: índice operativo basado en anomalías de SST (Niño 3.4)
- **Niño 1+2, 3, 3.4 y 4**: regiones oceánicas del Pacífico ecuatorial
- **MEI**: índice multivariado océano–atmósfera
- **SOI**: oscilación atmosférica asociada a la presión

El uso conjunto de estos índices permite un análisis **robusto y comparativo**.
""")

st.markdown("""
---

### 🌦️ Panorama Climático

Además del ENSO, el dashboard incorpora un **panorama climático general**, donde se
analizan:

- Distribución temporal de fases ENSO
- Intensidad de los eventos
- Variabilidad estacional
- Comportamiento histórico reciente (últimos 20 años)

Esto permite contextualizar el ENSO dentro del sistema climático.
""")

st.markdown("""
---

### 🧭 Estructura del Dashboard

El análisis se organiza en secciones:

1. **Clasificación ENSO** (fases e intensidad)
2. **Evolución temporal de índices**
3. **Distribuciones y valores extremos**
4. **Análisis estacional**
5. **Panorama climático integrado**

Cada sección puede explorarse de forma interactiva.
""")

st.info("📂 Utilizá el menú lateral para navegar entre las secciones del análisis.")
