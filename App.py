import streamlit as st
import pandas as pd

# secciones
page = st.sidebar.selectbox("Selecciona una página", ["Visualización de Datos", "Ingresar Datos"])


if page == "Visualización de Datos":

    # Título de la app
    st.title("Proceso E.D.A")

    # Subtítulo
    st.markdown("""
    El plan tiene dos fases. La primera es entrenar un modelo que prediga de manera satisfactoria si un cliente dado estará satisfecho o no ç
    con el producto en las categorías en las que se recoge ese dato. Mediante un análisis de importancia de características del modelo, 
    averiguar cuáles son las características que más influyen en la satisfacción del cliente y plasmar esos datos en un informe para negocio.
                La segunda es desarrollar una pequeña aplicación que recoja los datos de un cliente nuevo y realice una predicción sobre su grado de satisfacción.

    * **Librerías utilizadas:** pandas, streamlit, sklearn, 
    * **Repo
    * **etc
    * **etc
    """)

    # Cargar datos
    data = pd.read_csv('./Data/airline_passenger_satisfaction.csv')

    # Muestra el dataset como tabla

    st.subheader('Datos de satisfacción de clientes')
    st.dataframe(data)

else:  
    st.title("Página para Ingresar Datos")