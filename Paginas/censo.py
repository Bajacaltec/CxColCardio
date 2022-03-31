from mailbox import NoSuchMailboxError
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

def insertar():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    
    col1,col2,col3=st.columns(3)
    with col1:
        nombre=st.text_input("Nombre")
    with col2:
        edad=st.number_input("Edad",1,120)
    with col3:
        nss=st.number_input("NSS",1)
    with col1:
        capt=st.checkbox('Capturado')
        
    insertar=st.button("Insertar al censo")
    if insertar==True:
        try:
            cur.execute("INSERT INTO cxcolcardio VALUES (?,?,?,?)",(nombre,edad,nss,capt))
            con.commit()
            con.close()
        except:
            st.subheader("Paciente ya registrado")
    
def censo(base):
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select* FROM nombre''')
    dx=pd.read_sql_query("SELECT * from nombre", con)
    print(dx)
    st.dataframe(dx)
    con.close()

def promedio_edad():
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select avg(edad) FROM nombre''')
    edaddf=cur.fetchone()
    x,=edaddf
    st.subheader(x)
    
def capturado():
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    st.subheader("Capturado")
    sumedad=cur.execute('''Select sum(edad) FROM nombre''')
    edaddf=cur.fetchone()
    x,=edaddf
    st.subheader(x)
    
def crear_tabla(base):
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cxcolcardio
              (Nombre TEXT, Edad INT, NSS INT PRIMARY KEY, Diagnostico TEXT, Genero TEXT, Captura BOOL)''')
    con.commit()
    con.close()
    
def visualizacion():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    dxu=pd.read_sql_query("SELECT * from cxcolcardio", con)
    st.dataframe(dxu)
    con.commit()
    con.close
    
def buscar(id):
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    dxu=pd.read_sql_query("SELECT NSS from nombre", con)
    dyu=pd.read_sql_query("SELECT Nombre from nombre", con)
    col1,col2,col3=st.columns(3)
    with col1:
        igu=st.selectbox("NSS",(dxu))
    with col2:
        hu=st.selectbox("Nombre",(dyu))
        Yi=[hu]
    with col3:
        st.checkbox("Registrado")
        sumedad=cur.execute('''Select* FROM nombre WHERE Nombre=(?)''',(Yi))
        fe=cur.fetchone()
        st.text_input('Nombre',fe[0])
        st.number_input('Edad',fe[1])
        st.subheader(fe)
        borrar=st.button('Borrad')
        if borrar== True:
            sumedad=cur.execute('''DELETE FROM nombre WHERE Nombre=(?)''',(Yi))
            con.commit()
            con.close

        

      

    con.commit
    con.close
