import numpy as np
#from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'models/reclamos.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE RECOMENDACIÓN PARA CULTIVO </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #listas desplegables
    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    AG = st.text_input("AGENCIA:")
    P = st.text_input("Fósforo:")
    K = st.text_input("Potasio:")
    Temp = st.text_input("Temperatura:")
    Hum = st.text_input("Humedad:")
    pH = st.text_input("pH:")
    rai = st.text_input("Lluvia:")
    ra = st.text_input("Lluvia:")
    r = st.text_input("Lluvia:")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(AG.title()),
                    np.float_(P.title()),
                    np.float_(K.title()),
                    np.float_(Temp.title()),
                    np.float_(Hum.title()),
                    np.float_(pH.title()),
                    np.float_(rain.title()),
                    np.float_(rain.title()),
                    np.float_(rain.title()),
                    np.float_(rain.title())]
                                              
        predictS = model_prediction(x_in, model)
        st.success('EL CULTIVO RECOMENDADO ES: {}'.format(predictS[0]).upper())

if __name__ == '__main__':
    main()
