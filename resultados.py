from turtle import color, pensize, width
from pyparsing import col
from sqlalchemy import column
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
import altair as alt
from scipy import stats
plt.rcdefaults()
from scipy.stats import ttest_ind




def tabla1():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    #Tabla 1 características basales
    st.info('Tabla 1. Características basales de pacientes (medias) y su relación con la morbimortalidad')
    avg_edad_vivos=cur.execute('SELECT AVG(Edad) FROM Basecxcol WHERE Muerte = "No"')
    avg_edad_count,=cur.fetchone()
    
    av_edad_muertos=cur.execute('SELECT AVG(Edad) FROM Basecxcol WHERE Muerte = "Si" OR Comppostqx ="IV" OR Comppostqx= "V" ')
    avg_edad_count_muertos,=cur.fetchone()

    
    
    #Edad
    edad_array=cur.execute('SELECT Edad FROM Basecxcol WHERE Muerte="No"')
    edad_array_vivos=cur.fetchall()
    
    res = []
    for i in chain(*edad_array_vivos):
                res.append(i)

    edad_array_muertos=cur.execute('SELECT Edad FROM Basecxcol WHERE Muerte="Si"    ')
    edad_array_muertos_count=pd.array(cur.fetchall())
    des = []
    for i in chain(*edad_array_muertos_count):
                des.append(i)
    
    statcedad,pedad=stats.ttest_ind (a = res, b = des, equal_var = False)
    #Varianza
    #st.write(np.var(res),np.var(des))
    
    #Edad
    
    #Peso 
    #Peso vivos no complicados
    peso_db=cur.execute('SELECT Peso FROM Basecxcol WHERE Muerte="No"')
    peso_fetch=cur.fetchall()
    peso_num=[]
    for i in chain(*peso_fetch):
        peso_num.append(i)
        
    #Peso muertos complicados
    peso_mort_db=cur.execute('SELECT Peso FROM Basecxcol WHERe Muerte= "Si" OR Comppostqx="V" OR Comppostqx="IV" ')
    peso_mort_fetch=cur.fetchall()
    
    peso_num_mort=[]
    for i in chain(*peso_mort_fetch):
        peso_num_mort.append(i)
    
    avg_pesovivo=np.mean(peso_num)
    avg_pesomort=np.mean(peso_num_mort)
    
    statcpeso,pesos=stats.ttest_ind (a = peso_num, b = peso_num_mort, equal_var = False)

    #Peso
    
    #Talla
    talla_count=cur.execute('SELECT Talla FROM Basecxcol WHERE Muerte="No" AND Comppostqx!="IV" AND Comppostqx!="V"')
    talla_fetch=cur.fetchall()
    talla_np=[]
    for i in chain(*talla_fetch):
        talla_np.append(i)
    #talla muertos
    talla_count_mort=cur.execute('SELECT Talla FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV"')
    talla_fetch_mort=cur.fetchall()
    talla_mort=[]
    for i in chain(*talla_fetch_mort):
        talla_mort.append(i) 
    
    statctalla,tallas=stats.ttest_ind (a = talla_np, b = talla_mort, equal_var = False)

    #Talla
    
    #IMC
    IMC_count=cur.execute('SELECT IMC FROM Basecxcol WHERE Muerte="No" AND Comppostqx!="IV" AND Comppostqx!="V"')
    imc_fetch=cur.fetchall()
    imc_vivos=[]
    for i in chain(*imc_fetch):
        imc_vivos.append(i)
    
    IMC_count_mort=cur.execute('SELECT IMC FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="IV" OR Comppostqx="V"')
    imc_fetch_mort=cur.fetchall()
    imc_mort=[]
    for i in chain(*imc_fetch_mort):
        imc_mort.append(i)
        
    statcIMC,IMCp=stats.ttest_ind (a = imc_vivos, b = imc_mort, equal_var = False)

    
    
    
    Tabla_1_data=[avg_edad_count,avg_edad_count_muertos,pedad],[avg_pesovivo,avg_pesomort,pesos],[np.mean(talla_np),np.mean(talla_mort),tallas],[np.mean(imc_vivos),np.mean(imc_mort),IMCp]
    index_tabla1=['Edad','Peso (kg)','Talla (m)','IMC(m2)']
    column_tabla_1=['Supervivientes','Muerte','p']
    tabla_1=pd.DataFrame(Tabla_1_data,index_tabla1,column_tabla_1)

    st.dataframe(tabla_1)

    

  