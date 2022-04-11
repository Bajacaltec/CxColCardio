from operator import truth
from tkinter import Menu
import streamlit as st
from sympy import true
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
import Captura
  




con = sqlite3.connect('/Users/alonso/CxColCardio/otraprueba.db')
cur = con.cursor()
menú=st.sidebar.selectbox("Menú",['Censo','Capturar datos','Resultados'])
st.sidebar.image("/Users/alonso/CxColCardio/Paginas/Imagenes/CMN SXXI.jpeg", None)
    
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
            nem=(st.text_input('Nombre completo'))
            nombre=nem.upper()
            NeSS=st.text_input("NSS (10 digitos de NSS,ej. 10101010101F89OR","",16)
            NSS=NeSS.upper()
            Genero = "F" in NSS
            if Genero == True:
            #Para modificar el markdown con HTML se usa ese codigo de abajo
            #willkomen = '<p style="font-family:Times; color:Brown; font-size: 60px;">Bienvenida</p>'
            #st.markdown(willkomen, unsafe_allow_html=True)
                Genero = "Femenino"
                st.write("Bienvenida", " se esta completando el registro de ", nombre)
            else:
                st.write("Bienvenido", " se esta completando el registro de", nombre)
                Genero = "Masculino"
            edad=st.number_input('Edad',1,120,1,1)
            prediagnostico=st.multiselect('Diagnóstico',['CCLA','Colelitiasis','Piocolecisto','Colecistitis alitiásica','Colasco','Hidrocolecisto'])
            #no se pueden grabar listas en sql, con repr se hacen strings y se guardan, para separarlos tendremos que utilizar otro codigo posteriormente
            diagnostico=repr(prediagnostico)
            captura=st.checkbox('Capturado')
            fecha=st.date_input("Fecha de ingreso")

            regis_censo=st.button("Registrar en el censo")
            if regis_censo==True:
                censo.insertar(nombre,edad,NSS,diagnostico,Genero,fecha,captura)
    with st.expander('Censo',expanded=True):
        censo.visualizacion ()


elif menú=='Capturar datos':
    Captura.ficha_id()
    Captura.antecedentes()
    Captura.vitales_ingreso()
    Captura.labs_ingreso()
    Captura.SOFA()
    Captura.sintomas_ccla()
    Captura.labs_preqx()
    Captura.datos_cirugia()
    Captura.datos_postcirugia()
    Captura.registrarcapturaenbase()
    
elif menú=="Censo":
    censo.insertar()
    censo.censo()
    censo.promedio_edad()
    censo.crear_tabla()
    censo.buscar()


elif menú=='Resultados':
    st.image('resultados.png',None,400)
    resultados.edad()
    resultados.contar_genero()
    
        
        
    

    
    
    
    
