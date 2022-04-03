from operator import truth
from tkinter import Menu
import streamlit as st
from sympy import true
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import Paginas.censo as censo
import resultados
from functools import reduce
import numpy
import operator
from itertools import chain
  




con = sqlite3.connect('/Users/alonso/CxColCardio/otraprueba.db')
cur = con.cursor()
menú=st.sidebar.selectbox("Menú",['Censo','Capturar datos','Resultados'])
st.sidebar.image("/Users/alonso/CxColCardio/Paginas/Imagenes/CMN SXXI.jpeg", None)

censo.crear_tabla()

    

#Censo, incluye la tabla de los pacientes del estudio, seleccionar y borrar datos
if menú=='Censo':
    st.image('Censo.png',None,200)

    col1,col2=st.columns(2)
    with col1:
        with st.expander("Buscar"):
            con = sqlite3.connect('Basededatos.db')
            cur = con.cursor()
            sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
            nom=cur.fetchall()
            nombre=st.selectbox('Nombre',nom) 
            busqueda=st.checkbox('Buscar')
            if busqueda==True:
                censo.buscar(nombre)
    fol1,fol2,fol3=st.columns(3)
    
    #Expander para registrar paciente
    with col2:
        with st.expander('Registrar paciente'):
            nombre=st.text_input('Nombre completo')
            NSS=st.text_input("NSS")
            edad=st.number_input('Edad',1,120,1,1)
            prediagnostico=st.multiselect('Diagnóstico',['CCLA','Colelitiasis','Piocolecisto','Colecistitis alitiásica','Colasco','Hidrocolecisto'])
            #no se pueden grabar listas en sql, con repr se hacen strings y se guardan, para separarlos tendremos que utilizar otro codigo posteriormente
            diagnostico=repr(prediagnostico)
            genero=st.text_input('Genero')
            captura=st.checkbox('Capturado')
            fecha=st.date_input("Fecha de ingreso")

            regis_censo=st.button("Registrar en el censo")
            if regis_censo==True:
                censo.insertar(nombre,edad,NSS,diagnostico,genero,fecha,captura)
    
        
    censo.visualizacion ()


elif menú=='Capturar datos':
    st.subheader('Captura de datos')

elif menú=='Resultados':
    st.image('resultados.png',None,400)
    resultados.edad()
    resultados.contar_genero()
    
        
        
    

    
    
    
    
