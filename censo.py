import streamlit as st
import sqlite3
import pandas as pd
def insertar():
    con = sqlite3.connect('censo.db')
    cur = con.cursor()
    
    col1,col2,col3=st.columns(3)
    with col1:
        nombre=st.text_input("Nombre")
    with col2:
        edad=st.number_input("Edad",1,120)
    with col3:
        nss=st.number_input("NSS",1)
    insertar=st.button("Insertar al censo")
    if insertar==True:
        cur.execute("INSERT INTO nombre VALUES (?,?,?)",(nombre,edad,nss))
        con.commit()
        con.close()
    
def censo():
    con = sqlite3.connect('censo.db')
    cur = con.cursor()
    sumedad=cur.execute('''Select* FROM nombre''')
    df=sumedad.fetchone()
    for row in df:
        col1,col2=st.columns(2)
        with col1:
            st.subheader(df)
        with col2:
            st.checkbox('Censado')
    con.close() 
    