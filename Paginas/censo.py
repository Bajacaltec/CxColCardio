from mailbox import NoSuchMailboxError
from tkinter.filedialog import dialogstates
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np

def insertar(nombre,edad,NSS,diagnostico,genero,fecha,captura,hosp):
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()

    cur.execute("INSERT INTO cxcolcardio VALUES (?,?,?,?,?,?,?,?)",(nombre,edad,NSS,diagnostico,genero,fecha,captura,hosp))
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
              (Nombre TEXT, Edad INT, NSS TEXT PRIMARY KEY, Diagnostico TEXT, Genero TEXT, Fecha DATE, Captura TEXT)''')
    con.commit()
    con.close()
    
def visualizacion():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    dxy=cur.execute("SELECT * from cxcolcardio order by Nombre")
    dxu=pd.read_sql_query("SELECT * from cxcolcardio order by Nombre", con)
    wyu=cur.fetchall()
    g=['Nombre','Edad','NSS','Diagnóstico','Genero','Fecha','Capturado','Hospital']
    ju=pd.DataFrame(wyu,None,columns=g)
    st.dataframe(ju)
    con.commit()
    con.close
    
def buscar(nombre):
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()   
    sumedad=cur.execute('''Select *  FROM cxcolcardio WHERE Nombre=(?)''',(nombre))
    fe=cur.fetchall()
    st.success('Resultados de búsqueda')
    st.dataframe(fe)
   
    borrar=st.button('Borrar')
    if borrar== True:
        sumedad=cur.execute('''DELETE FROM cxcolcardio WHERE Nombre=(?)''',(nombre))
        st.error("Registro borrado")
        con.commit()
        con.close
        

def nombre_base():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
    edaddf=cur.fetchall()
    x,=edaddf
    st.subheader(x) 

      
def modificar():
    
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
    fe=cur.fetchall()
    nombre=st.selectbox('Buscar paciente',fe,)
    recabar=cur.execute("SELECT * FROM cxcolcardio WHERE Nombre = (?)",(nombre))
    fa,=cur.fetchall()
    nom_modificar=st.text_input('Nombre',fa[0])
    edad_modificar=st.number_input('Edad',fa[1])
    nss_modificar=st.text_input('NSS',fa[2])
    dx_modificar=st.text_input('Diagnóstico',fa[3])
    gen_modificar=st.text_input('Género',fa[4])
    fecha_modificar=st.text_input('Fecha',fa[5])
    captura_modificar=st.checkbox('Capturado',fa[6])
    st.markdown('Hospital')
    st.warning([fa[7]])
    hospital_modificar=st.selectbox('Modificar hospital',['Especialidades','H.Cardio','Ambos'])
    insertar_datos=st.button('Modificar Registro')
    #El WHERE toma la última variable que se pone en los paréntesis
    if insertar_datos==True:
            cur.execute("UPDATE cxcolcardio SET Nombre=?,Edad=?,NSS=?,Diagnostico=?,Genero=?,Fecha=?,Captura=?,Hospital=? WHERE Nombre=?",(nom_modificar,edad_modificar,nss_modificar,dx_modificar,gen_modificar,fecha_modificar,captura_modificar,hospital_modificar,nom_modificar))
            st.success('Modificación exitosa')
            st.balloons()
            con.commit()
    

        
    con.commit()
    con.close()
   
    
    