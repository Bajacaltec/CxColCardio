import streamlit as st
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import Paginas.censo as censo
#Base de datos
con = sqlite3.connect('/Users/alonso/CxColCardio/otraprueba.db')
cur = con.cursor()
st.sidebar.image("/Users/alonso/CxColCardio/Paginas/Imagenes/CMN SXXI.jpeg", None)
st.sidebar.text_input('Nombre completo')
st.sidebar.number_input("NSS",1,1111111111)
st.sidebar.text_input("Agregado abreviado (Ejem 1F89OR)")
menú=st.sidebar.selectbox("Menú",['Censo','Registro','Resultados'])
st.subheader(menú)

#Censo, incluye la tabla de los pacientes del estudio, seleccionar y borrar datos
if menú=='Censo':
    base='Basededatos.db'
    opciones_menu=st.selectbox('Opciones (censo)',['Visualización de censo','Buscar paciente','Registrar paciente'])
    if opciones_menu=='Visualización de censo':
        censo.visualizacion ()
    elif opciones_menu=='Registrar paciente':
        censo.insertar()
    
    
