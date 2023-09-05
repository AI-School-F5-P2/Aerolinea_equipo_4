import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        my_pipeline = pickle.load(file)
    return my_pipeline

my_pipeline = load_model()

model = my_pipeline["mdl"]
satisfaction_mapping = my_pipeline["satisfaction_mapping"]
OH_enc = my_pipeline["OH_enc"]
scaler = my_pipeline["scaler"]

def show_predict_page():
    st.title("Formulario satisfacción de clientes")

    st.write("""### Por favor complete nuestra encuesta para evaluar la calidad de nuestros servicios. 
                Le llevará un máximo de 10 minutos y nos ayudará a mejorar la calidad de los servicios que brindamos.""")


    Género  = (
        "Mujer",
        "Hombre",
    )

    Customer_Type = (
        "cliente leal",
        "cliente desleal",
    )
    Type_of_Travel = ( 
        'Viaje Personal',
        'Viaje de Negocio',
    )
    Class = (
        'Business', 
        'Eco', 
        'Eco Plus',
    )

    Género = st.selectbox("Género", Género)
    Customer Type = st.selectbox(" Customer Type",  Customer Type)
    Type of Travel = st.selectbox(" Type of Travel",  Type of Travel)
    Class = st.selectbox("Class",  Class)

    #Age = st.slider("Age", 0, 100, 3)

    #ok = st.button("Calculate Salary")
    #if ok:
        #X = np.array([[country, education, expericence ]])
        #X[:, 0] = le_country.transform(X[:,0])
        #X[:, 1] = le_education.transform(X[:,1])
        #X = X.astype(float)

        #salary = regressor.predict(X)
        #st.subheader(f"The estimated salary is ${salary[0]:.2f}")