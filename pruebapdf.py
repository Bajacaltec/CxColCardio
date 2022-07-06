from distutils.log import error
from email.policy import default
from locale import ALT_DIGITS
from operator import index
from matplotlib.pyplot import connect
from nbformat import write
from sqlalchemy import true
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3

from sympy import PythonIntegerRing
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
from itertools import chain
from Paginas.apache import PAM, creatdef, cronicos, cronicospreqx, edas, fcdef, htodef, kdef, leut, nadef, oxigen,frdef, phdef

from Paginas.apache import tempdef
from Paginas.censo import insertar
st.set_page_config(layout="wide",initial_sidebar_state='collapsed')      
        
def prueba():
    col1,col2=st.columns(2)
    with col1:
        with st.expander('Identificación y somatometría',True):
            con = sqlite3.connect('DB.db')
            cur = con.cursor()

            sumedad=cur.execute('''Select Nombre FROM Basecxcol''')
            nom=cur.fetchall()
            res = []
            for i in chain(*nom):
                res.append(i)
            
            nombre=(st.selectbox('Nombre',res), )
            nambre=str(nombre)
            numbre=nambre.replace("('","")
            global nimbre
            nimbre=(numbre.replace("',)",""),)

            cen = sqlite3.connect('DB.db')
            cor = cen.cursor()
            cor.execute("SELECT * FROM Basecxcol WHERE Nombre=(?)",(nimbre))
            global bes
            bes=cor.fetchall()
            st.sidebar.write(bes)
            bhu=str(bes)
            bhe=bhu.replace("(","")
            bhi=bhe.replace("('","")
            global bestrim
            bestrim=bhi.split(",")
            
                
                
def antecedentes():
    
    #intentar precargar datos ya capturados, except solo dejar defaults
        #st.write(bes)
       
        #x = bast.replace("[", "")
        #g=x.replace("]","")
        #j=g.replace(" '","")
        #k=j.replace("'","")
        #p=k.replace(' "',"")
        #suy=k.split(",")
        #st.write(suy)
            
      
        #este codigo limpia el string para que pueda ser utilizado por el multiselect, falta programar todos los demas, y dejarlo con un try y except por los errores en los que no tienen captura
    
   
        
        #ver como cargar los datos que ya estan en la base de datos en el formulario para poderlos modificar según 
        #la captura, arriba tengo como seleccionar datos de la base de datos final 
        #el problema es en las opciones de multiselect como pasarlos para que tengan  las capturas múltiples
    try:
        with st.expander('Antecedentes'):
            col1,col2,col3=st.columns(3)
        with col1:
            global comor
            comor = str(st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia","Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Miocarditis","Miocardiopatia dilatada","Otros"]))
        with col2:
            global tab
            st.write
            tab=st.selectbox("Tabaquismo",['No','Si'])
            if tab=='Si':
                global cajetillas
                cajetillas=st.number_input("Cajetillas/año",1,7000,1,1)
            else:
                cajetillas='NA'
            global cronicosapache
        with col3:
            cronicosapache=str(st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos']))
        with col1:
            global Tipocxcardio
            Tipocxcardio =str(st.multiselect("Procedimientos cardiovasculares", [
                                            "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"]))
        with col2:
            global usovasopr
            usovasopr = str(st.selectbox("Uso de vasopresores previos a cirugía por CCLA", ["No", "Si"]))
            if usovasopr == "Si":
                global tipovasopr
                tipovasopr = str(st.multiselect("Que vasopresor se utilizó", ["Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"]))
            else:
                tipovasopr='NA'
        with col3:
            global ventprol
            ventprol = st.number_input(
                    "Días con ventilación mecánica previo a cirugía", 0, 100, 0, 1)
        with col1:
            global uciestpreop
            uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)  