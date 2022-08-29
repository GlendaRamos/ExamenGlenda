# Import python libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from streamlit_option_menu import option_menu
from sqlalchemy import create_engine

# Page Layout
st.set_page_config(page_title="Emisiones de CO2 de fuentes estacionarias")

# CSS code to improve the design of the web app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Ttile of app
st.title("Emisiones de CO2 de fuentes estacionarias :link:")

st.write("---")

st.markdown(
    """La contaminación atmosférica es la suma de las emisiones en fuentes fijas y las emisiones de fuentes móviles. 
    Se pueden considerar fuentes fijas a la industria o actividad que genera quemas abiertas controladas en zonas 
    rurales, así como descargas de humos, gases, vapores, polvos o partículas por ductos o chimeneas, a emisiones 
    fugitivas o dispersas de contaminantes por actividades de explotación minera a cielo abierto, se incluye 
    incineración, procesos susceptibles de producir emisiones de sustancias tóxicas, producción de lubricantes y 
    combustibles, refinación y almacenamiento de petróleo y sus derivados, así como procesos fabriles petroquímicos,
     operaciones de plantas termoeléctricas, industria química, reactores nucleares, etc. 
 - **Python Libraries:** streamlit, pandas, numpy, plotly
 """
)

# Fill in information about the project implemented in this app
expander_bar = st.expander("About")
expander_bar.write(
    "Emisiones son todos los fluidos gaseosos, puros o con sustancias en suspensión; así como toda forma de energía "
    "radioactiva, electromagnética o sonora, que emanen como residuos o productos de la actividad humana y "
    "o natural (por ejemplo: las plantas emiten CO2)"
)

# Insert image
image = Image.open("resources/CO2.jpg")
st.image(image, width=100, use_column_width=True)


# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "Plots"],
        icons=["house", "clipboard-data", "tv"],
    )


# Call file if exist
if options == "Data":
    st.header("Dataframe de emisiones de CO2")
    engine = create_engine('sqlite:///CO2_EOR.db')
    df = pd.read_sql_query("SELECT* FROM R_Shushufindi", engine)
    st.dataframe(df)


