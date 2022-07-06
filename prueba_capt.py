from sqlalchemy import true
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
from itertools import chain
from Paginas.apache import PAM, creatdef, cronicos, cronicospreqx, edas, fcdef, htodef, kdef, leut, nadef, oxigen,frdef, phdef
from Paginas.apache import tempdef
from Paginas.censo import insertar

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
        bes,=cor.fetchall()
        
       
        st.sidebar.write(bes)
        global NSS
        NSS=st.text_input("NSS",bes[2])
        global edad
        bestrim_edad=int(bes[1])
        edad=st.number_input('Edad',1,200,bestrim_edad,key='987')
        bestrim_peso=int(bes[3])
        global peso
        peso = st.number_input("Peso",1,800,bestrim_peso,key='829')
        global talla
        bestrim_talla=float(bes[4])
        talla = st.number_input("Talla", 0.1, None, bestrim_talla, 0.1)
        bestrim_imc=float(bes[5])
        global imc
        indiceMC = st.number_input("IMC",None,None,bestrim_imc,0.1,disabled=True)
        st.success('')
    
with col2:
    with st.expander('Comentarios'):
        con=sqlite3.connect('DB.db')
        cur=con.cursor()
        cur.execute("SELECT Comentarios FROM Basecxcol WHERE Nombre=?",(nimbre))
        coment_base,=cur.fetchone()
        coment=st.text_area('Actualizar comentario',coment_base,350)
        actual_boton=st.button('Actualizar')
        if actual_boton==True:
            con=sqlite3.connect('DB.db')
            cur=con.cursor()
            cur.execute("""UPDATE Basecxcol SET Comentarios2=? WHERE Nombre=?""",(coment,nimbre))
            st.success('Actualizado')
            con.commit()
            con.close()
        
with st.expander('Antecedentes'):
    col1,col2,col3=st.columns(3)
    with col1:
        global comor
        comor=st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia","Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Miocarditis","Miocardiopatia dilatada","Otros"]) 
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
        cronicosapache=st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos'])
    with col1:
        global Tipocxcardio
        Tipocxcardio =st.multiselect("Procedimientos cardiovasculares", [
                                        "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"])
    with col2:
        global usovasopr
        usovasopr = st.selectbox("Uso de vasopresores previos a cirugía por CCLA", ["No", "Si"])
        if usovasopr == "Si":
            global tipovasopr
            tipovasopr = st.multiselect("Que vasopresor se utilizó", ["Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
        else:
            tipovasopr='NA'
    with col3:
        global ventprol
        ventprol = st.number_input(
                "Días con ventilación mecánica previo a cirugía", 0, 100, 0, 1)
    with col1:
        global uciestpreop
        uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)