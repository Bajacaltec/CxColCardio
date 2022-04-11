from turtle import width
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def manipular_base():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    select=st.selectbox('Selecciona',(['Consuelo','Alberto']))
    otraslect=st.selectbox('otra seleccion',['Edad','NSS'])
    promedad=cur.execute('''Select * FROM cxcolcardio WHERE Nombre=(?)''',(select))
    avgedad=promedad.fetchall()
    st.subheader(promedad)
    con.commit()
    st.subheader(avgedad)
    prom=avgedad[0]
    st.subheader(prom)
    suma,eda=prom
    d=[suma,eda]
    st.subheader(d)
    #Asignar un nombre a la columna con la variable como valor en un dictionario
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    f=['Promedio de edad','Suma edad']
    st.subheader("Edad")
    col1,col2=st.columns(2)
    with col1:
        dx=pd.DataFrame(d,f)
        st.bar_chart(dx)
    with col2:
        st.dataframe(dx)
    con.commit()
    con.close()
        
def edad():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    promedad=cur.execute('''Select avg(Edad),sum(Edad) FROM cxcolcardio''')
    avgedad=promedad.fetchall()
    prom=avgedad[0]
    suma,eda=prom    

    
    con.commit()
    #Asignar un nombre a la columna con la variable como valor en un dictionario
    d=[suma,eda]
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    f=['Promedio de edad','Suma edad']
    st.subheader("Edad")
    col1,col2=st.columns(2)
    with col1:
        dx=pd.DataFrame(d,f)
        st.bar_chart(dx)
    with col2:
        st.dataframe(dx)
    
    con.commit()
    con.close()

def contar_genero():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    MASC=cur.execute('''SELECT COUNT(*) FROM cxcolcardio WHERE Genero = 'Masculino' ''')
    Mgen=MASC.fetchone()
    masc,=Mgen
    FEM=cur.execute('''SELECT COUNT(*) FROM cxcolcardio WHERE Genero = 'Femenino' ''')
    Fgen=FEM.fetchone()
    fem,=Fgen
    df=([masc,fem])
    ind=['Masculino','Femenino']
    st.subheader('Genero')
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    dx=pd.DataFrame(df,ind)
    col1,col2=st.columns(2)
    with col1:
        st.bar_chart(dx)
    with col2:
        st.dataframe(dx)

    
      

