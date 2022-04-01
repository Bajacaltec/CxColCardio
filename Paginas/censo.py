from mailbox import NoSuchMailboxError
from tkinter.filedialog import dialogstates
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

def insertar(nombre,edad,NSS,diagnostico,genero,captura):
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    cur.execute("INSERT INTO cxcolcardio VALUES (?,?,?,?,?,?)",(nombre,edad,NSS,diagnostico,genero,captura))
    con.commit()
    con.close()
    st.subheader("Paciente ya registrado")
    st.balloons()
    
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
    
def crear_tabla():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS cxcolcardio
              (Nombre TEXT, Edad INT, NSS TEXT PRIMARY KEY, Diagnostico TEXT, Genero TEXT, Captura TEXT)''')
    con.commit()
    con.close()
    
def visualizacion():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    dxu=pd.read_sql_query("SELECT * from cxcolcardio", con)
    st.table(dxu)
    con.commit()
    con.close
    
def buscar(nombre):
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()   
    sumedad=cur.execute('''Select *  FROM cxcolcardio WHERE Nombre=(?)''',(nombre))
    fe=cur.fetchall()
    st.success('Resultados de búsqueda')
    st.dataframe(fe)
    xer=cur.execute('''DELETE FROM cxcolcardio WHERE Captura=No''')
    con.commit()
    con.close()
    borrar=st.button('Borrar')
    if borrar== True:
        sumedad=cur.execute('''DELETE FROM cxcolcardio WHERE Nombre=(?)''',(nombre))
        con.commit()
        con.close
        

def nombre_base():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
    edaddf=cur.fetchall()
    x,=edaddf
    st.subheader(x) 

      
