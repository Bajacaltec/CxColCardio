from turtle import pensize, width
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
    global masc
    masc,=Mgen
    FEM=cur.execute('''SELECT COUNT(*) FROM cxcolcardio WHERE Genero = 'Femenino' ''')
    Fgen=FEM.fetchone()
    global fem
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

def antropometrico():
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    edaf=cur.execute('''SELECT avg(Edad) FROM Prueba9''')
    ed=edaf.fetchall()
    edas,=ed
    edafe,=edas
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    pes=cur.execute('''SELECT avg(Peso) FROM Prueba9''')
    peso,=pes.fetchall()
    pas,=peso
    st.subheader(peso)
    tall=cur.execute('''SELECT avg(Talla) FROM Prueba9''')
    talle,=tall.fetchall()
    telle,=talle
    imcbis=cur.execute('''SELECT avg(IMC) FROM Prueba9''')
    imc,=imcbis.fetchall()
    imcfin,=imc
    columna=['Peso','Talla','IMC'] # nombre de las
    df = pd.DataFrame({'Edad':[edafe,telle],'Peso':[pas,telle], #nombre y valores de los datos, al poner dos variables se ponen dos filas
                   'Talla':[telle,imcfin],
                   'IMC':[imcfin,pas]})
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    tes=cur.execute('''SELECT COUNT(*) FROM Prueba9 WHERE Vasopresores = 'Si' ''')
    tesc=tes.fetchone()
    st.write(tesc)
    # Create the index
    index_ = ['Promedio','index'] # nombre de las filas
    
    # Set the index
    df.index = index_ # adjudicar el index
    
    # Print the DataFrame
    st.dataframe(df)
    
    
        


