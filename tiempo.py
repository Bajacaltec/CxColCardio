import streamlit as st 
import sqlite3
import numpy as np 
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency


from resultado_final import kruskallwallis




def tablas_tiempo():
#Chatgpt
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()

    # ... Tu código para las consultas SQL ...

    # Corregir la extracción de datos
    Tmen7II = cur.execute('SELECT COUNT(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx<=7 AND (Comppostqx="I" OR Comppostqx="II")').fetchone()
    # Hacer lo mismo para las demás consultas
    Tmay7II = cur.execute('SELECT COUNT(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx>=8 AND (Comppostqx="I" OR Comppostqx="II")').fetchone()
        
    Tmen7III = cur.execute('SELECT COUNT(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx<=7 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")').fetchone()

    Tmas7III = cur.execute('SELECT COUNT(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx>=8 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")').fetchone()

    contingency_table = [[Tmen7II, Tmay7II], [Tmen7III, Tmas7III]]
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    # Construir el DataFrame con una lista de diccionarios
    data_dict = {
        'T < 7 < II': [Tmen7II],
        'T > 7 dias < II': [Tmay7II],
        'T < 7 dias > III': [Tmen7III],
        'T > 7 dias > III': [Tmas7III],
        'p': [p_value]
    }
    indexdftiempo=['n']

    df_inicial = pd.DataFrame(data_dict,index=indexdftiempo)

    # Mostrar el DataFrame transpuesto
    dfinver = df_inicial

    # Mostrar el DataFrame
    st.table(dfinver)

