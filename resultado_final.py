from ctypes.wintypes import PPOINT
from lib2to3.pgen2 import pgen
from locale import ALT_DIGITS
from modulefinder import packagePathMap
from statistics import mean, pvariance, variance
import statistics
from tkinter import PhotoImage
from turtle import color, pensize, width
from matplotlib.cbook import safe_first_element
from pyparsing import col
import scipy
from sqlalchemy import column, false, true
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
st.set_page_config(layout="wide")


def tabla_boquim_morbmorta():
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
   #Tabla de valores bioquímicos y su relación con la morbilidad y mortalidad
    st.info('Predictores bioquímicos de morbilidad')
    #Leucocitosis morb baja
    cur.execute('Select Leupreqx FROM Basecxcol WHERE (Leupreqx!=0 AND Comppostqx="I") OR (Leupreqx!=0 AND Comppostqx="II")')
    leu_morb_CDbaja=cur.fetchall()
    avg_leumorb=mean(leu_morb_CDbaja)
    varianz_leumorb=statistics.variance(leu_morb_CDbaja)
    ed_leumorbaja=statistics.stdev(leu_morb_CDbaja)
    x,leumorb_baja_shapiro,=stats.shapiro(leu_morb_CDbaja)
    
    #Leucocitosis morb alta
    cur.execute('Select Leupreqx FROM Basecxcol WHERE (Leupreqx!=0 AND Comppostqx="III") OR (Leupreqx!=0 AND Comppostqx="IV")')
    leu_morb_alta=cur.fetchall()
    avg_leumorb_alta=mean(leu_morb_alta)
    varianz_leumorb_alta=statistics.variance(leu_morb_alta)
    ed_leumor_alta=statistics.stdev(leu_morb_alta)
    
    
    #p Leu_morbimorta
    
    h,p_leumorb,=stats.mannwhitneyu(leu_morb_CDbaja,leu_morb_alta)
    
    
     #ADE morb baja
    cur.execute('Select ADEpreqx FROM Basecxcol WHERE (ADEpreqx!=0 AND Comppostqx="I") OR (ADEpreqx!=0 AND Comppostqx="II")')
    ADE_morb_CDbaja=cur.fetchall()
    avg_ADE_morb=mean(ADE_morb_CDbaja)
    varianz_ADE_morb=statistics.variance(ADE_morb_CDbaja)
    ed_ADE_morbaja=statistics.stdev(ADE_morb_CDbaja)
    x,ADE_morb_baja_shapiro,=stats.shapiro(ADE_morb_CDbaja)
    
    #ADE morb alta
    cur.execute('Select ADEpreqx FROM Basecxcol WHERE (ADEpreqx!=0 AND Comppostqx="III") OR (ADEpreqx!=0 AND Comppostqx="IV")')
    ADE_morb_alta=cur.fetchall()
    avg_ADE_morb_alta=mean(ADE_morb_alta)
    varianz_ADE_morb_alta=statistics.variance(ADE_morb_alta)
    ed_ADE_mor_alta=statistics.stdev(ADE_morb_alta)
    
    #p ADE morbimorta
    
    i,p_ademorb,=stats.mannwhitneyu(ADE_morb_CDbaja,ADE_morb_alta)
    
    
    
     #HTO morb baja
    cur.execute('Select HTOpreqx FROM Basecxcol WHERE (HTOpreqx!=0 AND Comppostqx="I") OR (HTOpreqx!=0 AND Comppostqx="II")')
    HTO_morb_CDbaja=cur.fetchall()
    avg_HTO_morb=mean(HTO_morb_CDbaja)
    varianz_HTO_morb=statistics.variance(HTO_morb_CDbaja)
    ed_HTO_morbaja=statistics.stdev(HTO_morb_CDbaja)
    x,HTO_morb_baja_shapiro,=stats.shapiro(HTO_morb_CDbaja)
    
    #HTO morb alta
    cur.execute('Select HTOpreqx FROM Basecxcol WHERE (HTOpreqx!=0 AND Comppostqx="III") OR (HTOpreqx!=0 AND Comppostqx="IV")')
    HTO_morb_alta=cur.fetchall()
    avg_HTO_morb_alta=mean(HTO_morb_alta)
    varianz_HTO_morb_alta=statistics.variance(HTO_morb_alta)
    ed_HTO_mor_alta=statistics.stdev(HTO_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p HTO morbimorta
    
    i,p_HTOmorb,=stats.mannwhitneyu(HTO_morb_CDbaja,HTO_morb_alta)
    
    
     #PLT morb baja
    cur.execute('Select Plaqpreqx FROM Basecxcol WHERE (Plaqpreqx!=0 AND Comppostqx="I") OR (Plaqpreqx!=0 AND Comppostqx="II")')
    PLT_morb_CDbaja=cur.fetchall()
    avg_PLT_morb=mean(PLT_morb_CDbaja)
    varianz_PLT_morb=statistics.variance(PLT_morb_CDbaja)
    ed_PLT_morbaja=statistics.stdev(PLT_morb_CDbaja)
    io,PLT_morb_baja_shapiro,=stats.shapiro(PLT_morb_CDbaja)
    
    #PLT morb alta
    cur.execute('Select Plaqpreqx FROM Basecxcol WHERE (Plaqpreqx!=0 AND Comppostqx="III") OR (Plaqpreqx!=0 AND Comppostqx="IV")')
    PLT_morb_alta=cur.fetchall()
    avg_PLT_morb_alta=mean(PLT_morb_alta)
    varianz_PLT_morb_alta=statistics.variance(PLT_morb_alta)
    ed_PLT_mor_alta=statistics.stdev(PLT_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p PLT morbimorta
    
    i,p_PLTmorb,=stats.mannwhitneyu(PLT_morb_CDbaja,PLT_morb_alta)
    
    
    
    
     #AST morb baja
    cur.execute('Select ASTpreqx FROM Basecxcol WHERE (ASTpreqx!=0 AND Comppostqx="I") OR (ASTpreqx!=0 AND Comppostqx="II")')
    AST_morb_CDbaja=cur.fetchall()
    avg_AST_morb=mean(AST_morb_CDbaja)
    varianz_AST_morb=statistics.variance(AST_morb_CDbaja)
    ed_AST_morbaja=statistics.stdev(AST_morb_CDbaja)
    ioi,AST_morb_baja_shapiro,=stats.shapiro(AST_morb_CDbaja)
    
    #AST morb alta
    cur.execute('Select ASTpreqx FROM Basecxcol WHERE (ASTpreqx!=0 AND Comppostqx="III") OR (ASTpreqx!=0 AND Comppostqx="IV")')
    AST_morb_alta=cur.fetchall()
    avg_AST_morb_alta=mean(AST_morb_alta)
    varianz_AST_morb_alta=statistics.variance(AST_morb_alta)
    ed_AST_mor_alta=statistics.stdev(AST_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p AST morbimorta
    
    iou,p_ASTmorb,=stats.mannwhitneyu(AST_morb_CDbaja,AST_morb_alta)
    
    
     #ALT morb baja
    cur.execute(
        'Select ALTpreqx FROM Basecxcol WHERE (ALTpreqx!=0 AND Comppostqx="I") OR (ALTpreqx!=0 AND Comppostqx="II")')
    ALT_morb_CDbaja = cur.fetchall()
    avg_ALT_morb = mean(ALT_morb_CDbaja)
    varianz_ALT_morb = statistics.variance(ALT_morb_CDbaja)
    ed_ALT_morbaja = statistics.stdev(ALT_morb_CDbaja)
    ioi, ALT_morb_baja_shapiro, = stats.shapiro(ALT_morb_CDbaja)

    #ALT morb alta
    cur.execute(
        'Select ALTpreqx FROM Basecxcol WHERE (ALTpreqx!=0 AND Comppostqx="III") OR (ALTpreqx!=0 AND Comppostqx="IV")')
    ALT_morb_alta = cur.fetchall()
    avg_ALT_morb_alta = mean(ALT_morb_alta)
    varianz_ALT_morb_alta = statistics.variance(ALT_morb_alta)
    ed_ALT_mor_alta = statistics.stdev(ALT_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p ALT morbimorta

    iou, p_ALTmorb, = stats.mannwhitneyu(ALT_morb_CDbaja, ALT_morb_alta)
    
    
    
     #Biltot morb baja
    cur.execute(
        'Select Biltotpreqx FROM Basecxcol WHERE (Biltotpreqx!=0 AND Comppostqx="I") OR (Biltotpreqx!=0 AND Comppostqx="II")')
    Biltot_morb_CDbaja = cur.fetchall()
    avg_Biltot_morb = mean(Biltot_morb_CDbaja)
    varianz_Biltot_morb = statistics.variance(Biltot_morb_CDbaja)
    ed_Biltot_morbaja = statistics.stdev(Biltot_morb_CDbaja)
    ioi, Biltot_morb_baja_shapiro, = stats.shapiro(Biltot_morb_CDbaja)

    #Bil tot morb alta
    cur.execute(
        'Select Biltotpreqx FROM Basecxcol WHERE (Biltotpreqx!=0 AND Comppostqx="III") OR (Biltotpreqx!=0 AND Comppostqx="IV")')
    Biltot_morb_alta = cur.fetchall()
    avg_Biltot_morb_alta = mean(Biltot_morb_alta)
    varianz_Biltot_morb_alta = 0
    ed_Biltot_mor_alta = 0
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Biltot morbimorta

    iouw, p_Biltotmorb, = stats.mannwhitneyu(Biltot_morb_CDbaja, Biltot_morb_alta)



    
     #INR morb baja
    cur.execute(
        'Select INRpreqx FROM Basecxcol WHERE (INRpreqx!=0 AND Comppostqx="I") OR (INRpreqx!=0 AND Comppostqx="II")')
    INR_morb_CDbaja = cur.fetchall()
    avg_INR_morb = mean(INR_morb_CDbaja)
    varianz_INR_morb = statistics.variance(INR_morb_CDbaja)
    ed_INR_morbaja = statistics.stdev(INR_morb_CDbaja)
    ioi, INR_morb_baja_shapiro, = stats.shapiro(INR_morb_CDbaja)

    #INR  morb alta
    cur.execute(
        'Select INRpreqx FROM Basecxcol WHERE (INRpreqx!=0 AND Comppostqx="III") OR (INRpreqx!=0 AND Comppostqx="IV")')
    INR_morb_alta = cur.fetchall()
    avg_INR_morb_alta = mean(INR_morb_alta)
    varianz_INR_morb_alta = variance(INR_morb_alta)
    ed_INR_mor_alta = np.std(INR_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p INR morbimorta


    iouwe, p_INRmorb, = stats.mannwhitneyu(INR_morb_CDbaja, INR_morb_alta)
    
    
    
    
     #Creat morb baja
    cur.execute(
        'Select Creatpreqx FROM Basecxcol WHERE (Creatpreqx!=0 AND Comppostqx="I") OR (Creatpreqx!=0 AND Comppostqx="II")')
    Creat_morb_CDbaja = cur.fetchall()
    avg_Creat_morb = mean(Creat_morb_CDbaja)
    varianz_Creat_morb = statistics.variance(Creat_morb_CDbaja)
    ed_Creat_morbaja = statistics.stdev(Creat_morb_CDbaja)
    ioi, Creat_morb_baja_shapiro, = stats.shapiro(Creat_morb_CDbaja)

    #Creat  morb alta
    cur.execute(
        'Select Creatpreqx FROM Basecxcol WHERE (Creatpreqx!=0 AND Comppostqx="III") OR (Creatpreqx!=0 AND Comppostqx="IV")')
    Creat_morb_alta = cur.fetchall()
    avg_Creat_morb_alta = mean(Creat_morb_alta)
    varianz_Creat_morb_alta = variance(Creat_morb_alta)
    ed_Creat_mor_alta = np.std(Creat_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Creat morbimorta


    iouwey, p_Creatmorb, = stats.mannwhitneyu(Creat_morb_CDbaja, Creat_morb_alta)
    
    
    
    
    
    #Tiempoinsintqx morb baja
    cur.execute(
        'Select Tiempoinsintqx FROM Basecxcol WHERE (Tiempoinsintqx!=0 AND Comppostqx="I") OR (Tiempoinsintqx!=0 AND Comppostqx="II")')
    Tiempoinsintqx_morb_CDbaja = cur.fetchall()
    avg_Tiempoinsintqx_morb = mean(Tiempoinsintqx_morb_CDbaja)
    varianz_Tiempoinsintqx_morb = statistics.variance(Tiempoinsintqx_morb_CDbaja)
    ed_Tiempoinsintqx_morbaja = statistics.stdev(Tiempoinsintqx_morb_CDbaja)
    ioiae, Tiempoinsintqx_morb_baja_shapiro, = stats.shapiro(Tiempoinsintqx_morb_CDbaja)

    #Tiempoinsintqx  morb alta
    cur.execute(
        'Select Tiempoinsintqx FROM Basecxcol WHERE (Tiempoinsintqx!=0 AND Comppostqx="III") OR (Tiempoinsintqx!=0 AND Comppostqx="IV")')
    Tiempoinsintqx_morb_alta = cur.fetchall()
    avg_Tiempoinsintqx_morb_alta = mean(Tiempoinsintqx_morb_alta)
    varianz_Tiempoinsintqx_morb_alta = variance(Tiempoinsintqx_morb_alta)
    ed_Tiempoinsintqx_mor_alta = np.std(Tiempoinsintqx_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Tiempoinsintqx morbimorta


    iouweye, p_Tiempoinsintqxmorb, = stats.mannwhitneyu(Tiempoinsintqx_morb_CDbaja, Tiempoinsintqx_morb_alta)

    
    
    
    #qSOFApreqx morb baja
    cur.execute(
        'Select qSOFApreqx FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II")')
    qSOFApreqx_morb_CDbaja = cur.fetchall()
    avg_qSOFApreqx_morb = mean(qSOFApreqx_morb_CDbaja)
    varianz_qSOFApreqx_morb = statistics.variance(qSOFApreqx_morb_CDbaja)
    ed_qSOFApreqx_morbaja = statistics.stdev(qSOFApreqx_morb_CDbaja)
    ioiae, qSOFApreqx_morb_baja_shapiro, = stats.shapiro(qSOFApreqx_morb_CDbaja)

    #qSOFApreqx  morb alta
    cur.execute(
        'Select qSOFApreqx FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV")')
    qSOFApreqx_morb_alta = cur.fetchall()
    avg_qSOFApreqx_morb_alta = mean(qSOFApreqx_morb_alta)
    varianz_qSOFApreqx_morb_alta = variance(qSOFApreqx_morb_alta)
    ed_qSOFApreqx_mor_alta = np.std(qSOFApreqx_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p qSOFApreqx morbimorta


    iouweye, p_qSOFApreqxmorb, = stats.mannwhitneyu(qSOFApreqx_morb_CDbaja, qSOFApreqx_morb_alta)

    
    
    data_bio_morbimorta=[(leu_morb_CDbaja,avg_leumorb,leumorb_baja_shapiro,varianz_leumorb,ed_leumorbaja,leu_morb_alta,avg_leumorb_alta,'-',varianz_leumorb_alta,ed_leumor_alta,p_leumorb),
                         (ADE_morb_CDbaja,avg_ADE_morb,ADE_morb_baja_shapiro,varianz_ADE_morb,ed_ADE_morbaja,ADE_morb_alta,avg_ADE_morb_alta,'-',varianz_ADE_morb_alta,ed_ADE_mor_alta,p_ademorb),
                         (HTO_morb_CDbaja,avg_HTO_morb,HTO_morb_baja_shapiro,varianz_HTO_morb,ed_HTO_morbaja,HTO_morb_alta,avg_HTO_morb_alta,'-',varianz_HTO_morb_alta,ed_HTO_mor_alta,p_HTOmorb),
                         (PLT_morb_CDbaja,avg_PLT_morb,PLT_morb_baja_shapiro,varianz_PLT_morb,ed_PLT_morbaja,PLT_morb_alta,avg_PLT_morb_alta,'-',varianz_PLT_morb_alta,ed_PLT_mor_alta,p_PLTmorb),
                         (AST_morb_CDbaja,avg_AST_morb,AST_morb_baja_shapiro,varianz_AST_morb,ed_AST_morbaja,AST_morb_alta,avg_AST_morb_alta,'-',varianz_AST_morb_alta,ed_AST_mor_alta,p_ASTmorb),
                          (ALT_morb_CDbaja,avg_ALT_morb,ALT_morb_baja_shapiro,varianz_ALT_morb,ed_ALT_morbaja,ALT_morb_alta,avg_ALT_morb_alta,'-',varianz_ALT_morb_alta,ed_ALT_mor_alta,p_ALTmorb),
                          (Biltot_morb_CDbaja,avg_Biltot_morb,Biltot_morb_baja_shapiro,varianz_Biltot_morb,ed_Biltot_morbaja,Biltot_morb_alta,avg_Biltot_morb_alta,'-',varianz_Biltot_morb_alta,ed_Biltot_mor_alta,p_Biltotmorb),
                           (INR_morb_CDbaja,avg_INR_morb,INR_morb_baja_shapiro,varianz_INR_morb,ed_INR_morbaja,INR_morb_alta,avg_INR_morb_alta,'-',varianz_INR_morb_alta,ed_INR_mor_alta,p_INRmorb),
                            (Creat_morb_CDbaja,avg_Creat_morb,Creat_morb_baja_shapiro,varianz_Creat_morb,ed_Creat_morbaja,Creat_morb_alta,avg_Creat_morb_alta,'-',varianz_Creat_morb_alta,ed_Creat_mor_alta,p_Creatmorb),
                            (Tiempoinsintqx_morb_CDbaja,avg_Tiempoinsintqx_morb,Tiempoinsintqx_morb_baja_shapiro,varianz_Tiempoinsintqx_morb,ed_Tiempoinsintqx_morbaja,Tiempoinsintqx_morb_alta,avg_Tiempoinsintqx_morb_alta,'-',varianz_Tiempoinsintqx_morb_alta,ed_Tiempoinsintqx_mor_alta,p_Tiempoinsintqxmorb),
                            (qSOFApreqx_morb_CDbaja,avg_qSOFApreqx_morb,qSOFApreqx_morb_baja_shapiro,varianz_qSOFApreqx_morb,ed_qSOFApreqx_morbaja,qSOFApreqx_morb_alta,avg_qSOFApreqx_morb_alta,'-',varianz_qSOFApreqx_morb_alta,ed_qSOFApreqx_mor_alta,p_qSOFApreqxmorb)



                         ]
    index_biomorbimorta=['Leucocitosis (cel/mm3)','ADE','HTO','Plaquetas (cel/mm3)','AST (mg/dl)','ALT (mg/dl)','Bil tot (mg/dl)','INR',
                         'Creatinina (mg/dl)','Tiempo de evolución (dias)','qSOFA']
    col_biomorbimorta=['CD I y II','𝛍','Shapiro','Varianza val1','DE Val 1','CD III y IV','Val 2 𝛍','Shapiro val 2','Varianza val 2','DE val 2','p']
    global df_bioquim_morbimorta1

    df_bioquim_morbimorta1=pd.DataFrame(data_bio_morbimorta,index_biomorbimorta,col_biomorbimorta)
    st.dataframe(df_bioquim_morbimorta1)
    df_bioquim_morbimorta1.to_excel('/Users/alonso/CxColCardio/Tablafinal.xlsx',sheet_name='Tabla 1',index=false)
    
   



def tabla_boquim_morbmorta_2():
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
   #Tabla de valores bioquímicos y su relación con la morbilidad y mortalidad
    st.error('Predictores bioquímicos de Morbimorta')
    #Leucocitosis morb baja
    cur.execute('Select Leupreqx FROM Basecxcol WHERE (Leupreqx!=0 AND Comppostqx="I") OR (Leupreqx!=0 AND Comppostqx="II")')
    leu_morb_CDbaja=cur.fetchall()
    avg_leumorb=mean(leu_morb_CDbaja)
    varianz_leumorb=statistics.variance(leu_morb_CDbaja)
    ed_leumorbaja=statistics.stdev(leu_morb_CDbaja)
    x,leumorb_baja_shapiro,=stats.shapiro(leu_morb_CDbaja)
    
    #Leucocitosis morb alta
    cur.execute('Select Leupreqx FROM Basecxcol WHERE (Leupreqx!=0 AND Comppostqx="III") OR (Leupreqx!=0 AND Comppostqx="IV") OR (Leupreqx!=0 AND Comppostqx="V")')
    leu_morb_alta=cur.fetchall()
    avg_leumorb_alta=mean(leu_morb_alta)
    varianz_leumorb_alta=statistics.variance(leu_morb_alta)
    ed_leumor_alta=statistics.stdev(leu_morb_alta)
    ex,leumorb_alta_shapiro,=stats.shapiro(leu_morb_alta)

    
    
    #p Leu_morbimorta
    
    h,p_leumorb,=stats.mannwhitneyu(leu_morb_CDbaja,leu_morb_alta)
    
    
     #ADE morb baja
    cur.execute('Select ADEpreqx FROM Basecxcol WHERE (ADEpreqx!=0 AND Comppostqx="I") OR (ADEpreqx!=0 AND Comppostqx="II")')
    ADE_morb_CDbaja=cur.fetchall()
    avg_ADE_morb=mean(ADE_morb_CDbaja)
    varianz_ADE_morb=statistics.variance(ADE_morb_CDbaja)
    ed_ADE_morbaja=statistics.stdev(ADE_morb_CDbaja)
    x,ADE_morb_baja_shapiro,=stats.shapiro(ADE_morb_CDbaja)
    
    #ADE morb alta
    cur.execute('Select ADEpreqx FROM Basecxcol WHERE (ADEpreqx!=0 AND Comppostqx="III") OR (ADEpreqx!=0 AND Comppostqx="IV") OR (ADEpreqx!=0 AND Comppostqx="V")')
    ADE_morb_alta=cur.fetchall()
    avg_ADE_morb_alta=mean(ADE_morb_alta)
    varianz_ADE_morb_alta=statistics.variance(ADE_morb_alta)
    ed_ADE_mor_alta=statistics.stdev(ADE_morb_alta)
    ex,ADE_morb_alta_shapiro,=stats.shapiro(ADE_morb_alta)

    
    #p ADE morbimorta
    
    i,p_ademorb,=stats.ttest_ind(ADE_morb_CDbaja,ADE_morb_alta,equal_var=True)
    
    
    
     #HTO morb baja
    cur.execute('Select HTOpreqx FROM Basecxcol WHERE (HTOpreqx!=0 AND Comppostqx="I") OR (HTOpreqx!=0 AND Comppostqx="II")')
    HTO_morb_CDbaja=cur.fetchall()
    avg_HTO_morb=mean(HTO_morb_CDbaja)
    varianz_HTO_morb=statistics.variance(HTO_morb_CDbaja)
    ed_HTO_morbaja=statistics.stdev(HTO_morb_CDbaja)
    x,HTO_morb_baja_shapiro,=stats.shapiro(HTO_morb_CDbaja)
    
    #HTO morb alta
    cur.execute('Select HTOpreqx FROM Basecxcol WHERE (HTOpreqx!=0 AND Comppostqx="III") OR (HTOpreqx!=0 AND Comppostqx="IV") OR (HTOpreqx!=0 AND Comppostqx="V")')
    HTO_morb_alta=cur.fetchall()
    avg_HTO_morb_alta=mean(HTO_morb_alta)
    varianz_HTO_morb_alta=statistics.variance(HTO_morb_alta)
    ed_HTO_mor_alta=statistics.stdev(HTO_morb_alta)
    xx,HTO_morb_alta_shapiro,=stats.shapiro(HTO_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p HTO morbimorta
    
    i,p_HTOmorb,=stats.ttest_ind(HTO_morb_CDbaja,HTO_morb_alta,equal_var=True)
    
    
     #PLT morb baja
    cur.execute('Select Plaqpreqx FROM Basecxcol WHERE (Plaqpreqx!=0 AND Comppostqx="I") OR (Plaqpreqx!=0 AND Comppostqx="II")')
    PLT_morb_CDbaja=cur.fetchall()
    avg_PLT_morb=mean(PLT_morb_CDbaja)
    varianz_PLT_morb=statistics.variance(PLT_morb_CDbaja)
    ed_PLT_morbaja=statistics.stdev(PLT_morb_CDbaja)
    io,PLT_morb_baja_shapiro,=stats.shapiro(PLT_morb_CDbaja)
    
    #PLT morb alta
    cur.execute('Select Plaqpreqx FROM Basecxcol WHERE (Plaqpreqx!=0 AND Comppostqx="III") OR (Plaqpreqx!=0 AND Comppostqx="IV") OR (Plaqpreqx!=0 AND Comppostqx="V")')
    PLT_morb_alta=cur.fetchall()
    avg_PLT_morb_alta=mean(PLT_morb_alta)
    varianz_PLT_morb_alta=statistics.variance(PLT_morb_alta)
    ed_PLT_mor_alta=statistics.stdev(PLT_morb_alta)
    eio,PLT_morb_alta_shapiro,=stats.shapiro(PLT_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p PLT morbimorta
    
    i,p_PLTmorb,=stats.mannwhitneyu(PLT_morb_CDbaja,PLT_morb_alta)
    
    
    
    
     #AST morb baja
    cur.execute('Select ASTpreqx FROM Basecxcol WHERE (ASTpreqx!=0 AND Comppostqx="I") OR (ASTpreqx!=0 AND Comppostqx="II")')
    AST_morb_CDbaja=cur.fetchall()
    avg_AST_morb=mean(AST_morb_CDbaja)
    varianz_AST_morb=statistics.variance(AST_morb_CDbaja)
    ed_AST_morbaja=statistics.stdev(AST_morb_CDbaja)
    ioi,AST_morb_baja_shapiro,=stats.shapiro(AST_morb_CDbaja)
    
    #AST morb alta
    cur.execute('Select ASTpreqx FROM Basecxcol WHERE (ASTpreqx!=0 AND Comppostqx="III") OR (ASTpreqx!=0 AND Comppostqx="IV") OR (ASTpreqx!=0 AND Comppostqx="V")')
    AST_morb_alta=cur.fetchall()
    avg_AST_morb_alta=mean(AST_morb_alta)
    varianz_AST_morb_alta=statistics.variance(AST_morb_alta)
    ed_AST_mor_alta=statistics.stdev(AST_morb_alta)
    wioi,AST_morb_alta_shapiro,=stats.shapiro(AST_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    
    #p AST morbimorta
    
    iou,p_ASTmorb,=stats.mannwhitneyu(AST_morb_CDbaja,AST_morb_alta)
    
    
     #ALT morb baja
    cur.execute(
        'Select ALTpreqx FROM Basecxcol WHERE (ALTpreqx!=0 AND Comppostqx="I") OR (ALTpreqx!=0 AND Comppostqx="II")')
    ALT_morb_CDbaja = cur.fetchall()
    avg_ALT_morb = mean(ALT_morb_CDbaja)
    varianz_ALT_morb = statistics.variance(ALT_morb_CDbaja)
    ed_ALT_morbaja = statistics.stdev(ALT_morb_CDbaja)
    ioi, ALT_morb_baja_shapiro, = stats.shapiro(ALT_morb_CDbaja)

    #ALT morb alta
    cur.execute(
        'Select ALTpreqx FROM Basecxcol WHERE (ALTpreqx!=0 AND Comppostqx="III") OR (ALTpreqx!=0 AND Comppostqx="IV") OR (ALTpreqx!=0 AND Comppostqx="V")')
    ALT_morb_alta = cur.fetchall()
    avg_ALT_morb_alta = mean(ALT_morb_alta)
    varianz_ALT_morb_alta = statistics.variance(ALT_morb_alta)
    ed_ALT_mor_alta = statistics.stdev(ALT_morb_alta)
    gioi, ALT_morb_alta_shapiro, = stats.shapiro(ALT_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p ALT morbimorta

    iou, p_ALTmorb, = stats.mannwhitneyu(ALT_morb_CDbaja, ALT_morb_alta)
    
    
    
     #Biltot morb baja
    cur.execute(
        'Select Biltotpreqx FROM Basecxcol WHERE (Biltotpreqx!=0 AND Comppostqx="I") OR (Biltotpreqx!=0 AND Comppostqx="II")')
    Biltot_morb_CDbaja = cur.fetchall()
    avg_Biltot_morb = mean(Biltot_morb_CDbaja)
    varianz_Biltot_morb = statistics.variance(Biltot_morb_CDbaja)
    ed_Biltot_morbaja = statistics.stdev(Biltot_morb_CDbaja)
    ioi, Biltot_morb_baja_shapiro, = stats.shapiro(Biltot_morb_CDbaja)

    #Bil tot morb alta
    cur.execute(
        'Select Biltotpreqx FROM Basecxcol WHERE (Biltotpreqx!=0 AND Comppostqx="III") OR (Biltotpreqx!=0 AND Comppostqx="IV") OR (Biltotpreqx!=0 AND Comppostqx="V")')
    Biltot_morb_alta = cur.fetchall()
    avg_Biltot_morb_alta = mean(Biltot_morb_alta)
    varianz_Biltot_morb_alta = variance(Biltot_morb_alta)
    ed_Biltot_mor_alta = statistics.stdev(Biltot_morb_alta)
    ioi, Biltot_morb_alta_shapiro, = stats.shapiro(Biltot_morb_alta)
    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Biltot morbimorta

    iouw, p_Biltotmorb, = stats.ttest_ind(Biltot_morb_CDbaja, Biltot_morb_alta,equal_var=True)



    
     #INR morb baja
    cur.execute(
        'Select INRpreqx FROM Basecxcol WHERE (INRpreqx!=0 AND Comppostqx="I") OR (INRpreqx!=0 AND Comppostqx="II")')
    INR_morb_CDbaja = cur.fetchall()
    avg_INR_morb = mean(INR_morb_CDbaja)
    varianz_INR_morb = statistics.variance(INR_morb_CDbaja)
    ed_INR_morbaja = statistics.stdev(INR_morb_CDbaja)
    ioi, INR_morb_baja_shapiro, = stats.shapiro(INR_morb_CDbaja)

    #INR  morb alta
    cur.execute(
        'Select INRpreqx FROM Basecxcol WHERE (INRpreqx!=0 AND Comppostqx="III") OR (INRpreqx!=0 AND Comppostqx="IV") OR (INRpreqx!=0 AND Comppostqx="V")')
    INR_morb_alta = cur.fetchall()
    avg_INR_morb_alta = mean(INR_morb_alta)
    varianz_INR_morb_alta = variance(INR_morb_alta)
    ed_INR_mor_alta = np.std(INR_morb_alta)
    hioi, INR_morb_alta_shapiro, = stats.shapiro(INR_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p INR morbimorta


    iouwe, p_INRmorb, = stats.mannwhitneyu(INR_morb_CDbaja, INR_morb_alta)
    
    
    
    
     #Creat morb baja
    cur.execute(
        'Select Creatpreqx FROM Basecxcol WHERE (Creatpreqx!=0 AND Comppostqx="I") OR (Creatpreqx!=0 AND Comppostqx="II")')
    Creat_morb_CDbaja = cur.fetchall()
    avg_Creat_morb = mean(Creat_morb_CDbaja)
    varianz_Creat_morb = statistics.variance(Creat_morb_CDbaja)
    ed_Creat_morbaja = statistics.stdev(Creat_morb_CDbaja)
    ioi, Creat_morb_baja_shapiro, = stats.shapiro(Creat_morb_CDbaja)

    #Creat  morb alta
    cur.execute(
        'Select Creatpreqx FROM Basecxcol WHERE (Creatpreqx!=0 AND Comppostqx="III") OR (Creatpreqx!=0 AND Comppostqx="IV") OR (Creatpreqx!=0 AND Comppostqx="V")')
    Creat_morb_alta = cur.fetchall()
    avg_Creat_morb_alta = mean(Creat_morb_alta)
    varianz_Creat_morb_alta = variance(Creat_morb_alta)
    ed_Creat_mor_alta = np.std(Creat_morb_alta)
    rioi, Creat_morb_alta_shapiro, = stats.shapiro(Creat_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Creat morbimorta


    iouwey, p_Creatmorb, = stats.mannwhitneyu(Creat_morb_CDbaja, Creat_morb_alta)
    
    
    
    
    
    #Tiempoinsintqx morb baja
    cur.execute(
        'Select Tiempoinsintqx FROM Basecxcol WHERE (Tiempoinsintqx!=0 AND Comppostqx="I") OR (Tiempoinsintqx!=0 AND Comppostqx="II")')
    Tiempoinsintqx_morb_CDbaja = cur.fetchall()
    avg_Tiempoinsintqx_morb = mean(Tiempoinsintqx_morb_CDbaja)
    varianz_Tiempoinsintqx_morb = statistics.variance(Tiempoinsintqx_morb_CDbaja)
    ed_Tiempoinsintqx_morbaja = statistics.stdev(Tiempoinsintqx_morb_CDbaja)
    ioiae, Tiempoinsintqx_morb_baja_shapiro, = stats.shapiro(Tiempoinsintqx_morb_CDbaja)

    #Tiempoinsintqx  morb alta
    cur.execute(
        'Select Tiempoinsintqx FROM Basecxcol WHERE (Tiempoinsintqx!=0 AND Comppostqx="III") OR (Tiempoinsintqx!=0 AND Comppostqx="IV") OR (Tiempoinsintqx!=0 AND Comppostqx="V")')
    Tiempoinsintqx_morb_alta = cur.fetchall()
    avg_Tiempoinsintqx_morb_alta = mean(Tiempoinsintqx_morb_alta)
    varianz_Tiempoinsintqx_morb_alta = variance(Tiempoinsintqx_morb_alta)
    ed_Tiempoinsintqx_mor_alta = np.std(Tiempoinsintqx_morb_alta)
    dioiae, Tiempoinsintqx_morb_alta_shapiro, = stats.shapiro(Tiempoinsintqx_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p Tiempoinsintqx morbimorta


    iouweye, p_Tiempoinsintqxmorb, = stats.mannwhitneyu(Tiempoinsintqx_morb_CDbaja, Tiempoinsintqx_morb_alta)

    
    
    
    #qSOFApreqx morb baja
    cur.execute(
        'Select qSOFApreqx FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II")')
    qSOFApreqx_morb_CDbaja = cur.fetchall()
    avg_qSOFApreqx_morb = mean(qSOFApreqx_morb_CDbaja)
    varianz_qSOFApreqx_morb = statistics.variance(qSOFApreqx_morb_CDbaja)
    ed_qSOFApreqx_morbaja = statistics.stdev(qSOFApreqx_morb_CDbaja)
    ioiae, qSOFApreqx_morb_baja_shapiro, = stats.shapiro(qSOFApreqx_morb_CDbaja)

    #qSOFApreqx  morb alta
    cur.execute(
        'Select qSOFApreqx FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") OR (Comppostqx="V")')
    qSOFApreqx_morb_alta = cur.fetchall()
    avg_qSOFApreqx_morb_alta = mean(qSOFApreqx_morb_alta)
    varianz_qSOFApreqx_morb_alta = variance(qSOFApreqx_morb_alta)
    ed_qSOFApreqx_mor_alta = np.std(qSOFApreqx_morb_alta)
    ioiaeg, qSOFApreqx_morb_alta_shapiro, = stats.shapiro(qSOFApreqx_morb_alta)

    #No tengo Shapiro por que solo tengo dos pacientes con complicaciones III y IV

    #p qSOFApreqx morbimorta


    iouweye, p_qSOFApreqxmorb, = stats.mannwhitneyu(qSOFApreqx_morb_CDbaja, qSOFApreqx_morb_alta)

    
    
    data_bio_morbimorta=[(leu_morb_CDbaja,avg_leumorb,leumorb_baja_shapiro,varianz_leumorb,ed_leumorbaja,leu_morb_alta,avg_leumorb_alta,leumorb_alta_shapiro,varianz_leumorb_alta,ed_leumor_alta,p_leumorb),
                         (ADE_morb_CDbaja,avg_ADE_morb,ADE_morb_baja_shapiro,varianz_ADE_morb,ed_ADE_morbaja,ADE_morb_alta,avg_ADE_morb_alta,ADE_morb_alta_shapiro,varianz_ADE_morb_alta,ed_ADE_mor_alta,p_ademorb),
                         (HTO_morb_CDbaja,avg_HTO_morb,HTO_morb_baja_shapiro,varianz_HTO_morb,ed_HTO_morbaja,HTO_morb_alta,avg_HTO_morb_alta,HTO_morb_alta_shapiro,varianz_HTO_morb_alta,ed_HTO_mor_alta,p_HTOmorb),
                         (PLT_morb_CDbaja,avg_PLT_morb,PLT_morb_baja_shapiro,varianz_PLT_morb,ed_PLT_morbaja,PLT_morb_alta,avg_PLT_morb_alta,PLT_morb_alta_shapiro,varianz_PLT_morb_alta,ed_PLT_mor_alta,p_PLTmorb),
                         (AST_morb_CDbaja,avg_AST_morb,AST_morb_baja_shapiro,varianz_AST_morb,ed_AST_morbaja,AST_morb_alta,avg_AST_morb_alta,AST_morb_alta_shapiro,varianz_AST_morb_alta,ed_AST_mor_alta,p_ASTmorb),
                          (ALT_morb_CDbaja,avg_ALT_morb,ALT_morb_baja_shapiro,varianz_ALT_morb,ed_ALT_morbaja,ALT_morb_alta,avg_ALT_morb_alta,ALT_morb_alta_shapiro,varianz_ALT_morb_alta,ed_ALT_mor_alta,p_ALTmorb),
                          (Biltot_morb_CDbaja,avg_Biltot_morb,Biltot_morb_baja_shapiro,varianz_Biltot_morb,ed_Biltot_morbaja,Biltot_morb_alta,avg_Biltot_morb_alta,Biltot_morb_alta_shapiro,varianz_Biltot_morb_alta,ed_Biltot_mor_alta,p_Biltotmorb),
                           (INR_morb_CDbaja,avg_INR_morb,INR_morb_baja_shapiro,varianz_INR_morb,ed_INR_morbaja,INR_morb_alta,avg_INR_morb_alta,INR_morb_alta_shapiro,varianz_INR_morb_alta,ed_INR_mor_alta,p_INRmorb),
                            (Creat_morb_CDbaja,avg_Creat_morb,Creat_morb_baja_shapiro,varianz_Creat_morb,ed_Creat_morbaja,Creat_morb_alta,avg_Creat_morb_alta,Creat_morb_alta_shapiro,varianz_Creat_morb_alta,ed_Creat_mor_alta,p_Creatmorb),
                            (Tiempoinsintqx_morb_CDbaja,avg_Tiempoinsintqx_morb,Tiempoinsintqx_morb_baja_shapiro,varianz_Tiempoinsintqx_morb,ed_Tiempoinsintqx_morbaja,Tiempoinsintqx_morb_alta,avg_Tiempoinsintqx_morb_alta,Tiempoinsintqx_morb_alta_shapiro,varianz_Tiempoinsintqx_morb_alta,ed_Tiempoinsintqx_mor_alta,p_Tiempoinsintqxmorb),
                            (qSOFApreqx_morb_CDbaja,avg_qSOFApreqx_morb,qSOFApreqx_morb_baja_shapiro,varianz_qSOFApreqx_morb,ed_qSOFApreqx_morbaja,qSOFApreqx_morb_alta,avg_qSOFApreqx_morb_alta,qSOFApreqx_morb_alta_shapiro,varianz_qSOFApreqx_morb_alta,ed_qSOFApreqx_mor_alta,p_qSOFApreqxmorb)



                         ]
    index_biomorbimorta=['Leucocitosis (cel/mm3)','ADE','HTO','Plaquetas (cel/mm3)','AST (mg/dl)','ALT (mg/dl)','Bil tot (mg/dl)','INR',
                         'Creatinina (mg/dl)','Tiempo de evolución (dias)','qSOFA']
    col_biomorbimorta=['CD <III','𝛍','Shapiro','Varianza val1','DE Val 1','CD >III','Val 2 𝛍','Shapiro val 2','Varianza val 2','DE val 2','p']
    df_bioquim_morbimorta=pd.DataFrame(data_bio_morbimorta,index_biomorbimorta,col_biomorbimorta)
    st.dataframe(df_bioquim_morbimorta)
    
    #para mandar los archivos en hojas separadas hay que usar el writer de pandas
    with pd.ExcelWriter('/Users/alonso/CxColCardio/Tablafinal.xlsx') as writer:  
        df_bioquim_morbimorta1.to_excel(writer, sheet_name='Morbilidad y significancia')
        df_bioquim_morbimorta.to_excel(writer, sheet_name='Morbimorta significancia')

def tabla_ordinales():
    st.success('Variables ordinales')
    
    #ASA
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #ASAI
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="I" AND Comppostqx="I" ) OR (asa="I" AND Comppostqx= "II" )')
    asaI_baja=cur.fetchone()
    
    asaI_porcentaje_baja=asaI_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="I" AND Comppostqx="III" ) OR (asa="I" AND Comppostqx= "IV" )OR (asa="I" AND Comppostqx= "V" )')
    asaI_alta=cur.fetchone()
    
    asaI_porcentaje_alta=asaI_alta/18
    fish=stats.chi
    asaI_p='???'
    
    
    #ASAII
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="I" ) OR (asa="II" AND Comppostqx= "II" )')
    asaII_baja=cur.fetchone()
    
    asaII_porcentaje_baja=asaII_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="III" ) OR (asa="II" AND Comppostqx= "IV" )OR (asa="II" AND Comppostqx= "V" )')
    asaII_alta=cur.fetchone()
    
    asaII_porcentaje_alta=asaII_alta/18
    fish=stats.chi
    asaII_p='0.1362'
    
    
     #ASAIIII
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="I" ) OR (asa="III" AND Comppostqx= "II" )')
    asaIII_baja=cur.fetchone()
    
    asaIII_porcentaje_baja=asaIII_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="III" ) OR (asa="III" AND Comppostqx= "IV" )OR (asa="III" AND Comppostqx= "V" )')
    asaIII_alta=cur.fetchone()
    
    asaIII_porcentaje_alta=asaIII_alta/18
    asaIII_p='?'

    
    #ASA IV
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="I" ) OR (asa="IV" AND Comppostqx= "II" )')
    asaIV_baja=cur.fetchone()
    
    asaIV_porcentaje_baja=asaIV_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="III" ) OR (asa="IV" AND Comppostqx= "IV" )OR (asa="IV" AND Comppostqx= "V" )')
    asaIV_alta=cur.fetchone()
    
    asaIV_porcentaje_alta=asaIV_alta/18
    
    asaIV_p='?'
    
    #ASA V
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="V" AND Comppostqx="I" ) OR (asa="V" AND Comppostqx= "II" )')
    asaV_baja=cur.fetchone()
    
    asaV_porcentaje_baja=asaV_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="V" AND Comppostqx="III" ) OR (asa="V" AND Comppostqx= "IV" )OR (asa="V" AND Comppostqx= "V" )')
    asaV_alta=cur.fetchone()
    
    asaV_porcentaje_alta=asaV_alta/18
    
    asaV_p='?'
    
    
        #ASA VI
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="VI" AND Comppostqx="I" ) OR (asa="VI" AND Comppostqx= "II" )')
    asaVI_baja=cur.fetchone()
    
    asaVI_porcentaje_baja=asaVI_baja/18
    
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="VI" AND Comppostqx="III" ) OR (asa="VI" AND Comppostqx= "IV" )OR (asa="VI" AND Comppostqx= "V" )')
    asaVI_alta=cur.fetchone()
    
    asaVI_porcentaje_alta=asaVI_alta/18
    
    asaVI_p='?'

    
    data_asa=[(asaI_baja,asaI_porcentaje_baja,asaI_alta,asaI_porcentaje_alta,asaI_p),
              (asaII_baja,asaII_porcentaje_baja,asaII_alta,asaII_porcentaje_alta,asaII_p),
              (asaIII_baja,asaIII_porcentaje_baja,asaIII_alta,asaIII_porcentaje_alta,asaIII_p),
              (asaIV_baja,asaIV_porcentaje_baja,asaIV_alta,asaIV_porcentaje_alta,asaIV_p),
              (asaV_baja,asaV_porcentaje_baja,asaV_alta,asaV_porcentaje_alta,asaV_p),
            (asaVI_baja,asaVI_porcentaje_baja,asaVI_alta,asaVI_porcentaje_alta,asaVI_p),
]
    index_asa=['ASA I','ASA II','ASA III','ASA IV','ASA V','ASA VI']
    col_asa=['CD I y II','%','CD >III','%%','p']
    
    df_asa=pd.DataFrame(data_asa,index_asa,col_asa)
    obs_asa=np.array([[1.,4.,3.],[1.,4.,5.]])
    asaIII_pe=stats.chi2_contingency(obs_asa,)
    st.write(asaIII_pe)
    st.dataframe(df_asa)

def tabla_litiasis():
    st.info('Litiasis vs alitiasis')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #Litiasica
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tipoccla = "Litiasica") OR (Comppostqx = "II" AND Tipoccla = "Litiasica")')
    lit_morb_baja=cur.fetchone()
    
    #litiásica morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tipoccla = "Litiasica") OR (Comppostqx = "IV" AND Tipoccla = "Litiasica") OR (Comppostqx = "V" AND Tipoccla = "Litiasica")')
    lit_morb_alta=cur.fetchone()
    
    #aLitiasica
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tipoccla = "Alitiasica") OR (Comppostqx = "II" AND Tipoccla = "Alitiasica")')
    alit_morb_baja=cur.fetchone()
    
    #alitiásica morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tipoccla = "Alitiasica") OR (Comppostqx = "IV" AND Tipoccla = "Alitiasica") OR (Comppostqx = "V" AND Tipoccla = "Alitiasica")')
    alit_morb_alta=cur.fetchone()
    
    data_lit=[[alit_morb_baja,alit_morb_alta],[lit_morb_baja,lit_morb_alta]]
    x,ore,=stats.fisher_exact(data_lit)
    dt_lit=[(alit_morb_baja,alit_morb_baja/18,alit_morb_alta,alit_morb_alta/18,ore),
            (lit_morb_baja,lit_morb_baja/18,lit_morb_alta,lit_morb_alta/18)]
    index_lit=['Alitiásica','Litiásica']
    col_lit=[' CD I y II','Frec alit', ' CD >III',' Frec litiasica','p']
    df_lit=pd.DataFrame(dt_lit,index_lit,col_lit)
    st.dataframe(df_lit)

    
    
    
    #colecistitis aguda
    
    
    
    #hice una prueba de fishers con los datos de la cole liaitiasica vs alitiasica sale 
    #p de 1 es para una prueba de 2x2
    #    morb baja  morb alta
    #lit
    #alit
    
    
def tokyo_categórica():
    st.info('Tokyo-morbimorta')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #tokyo leve
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Leve") OR (Comppostqx = "II" AND Tokyo = "Leve")')
    tokyo_morb_baja=cur.fetchone()
    
    #tokyo leve morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Leve") OR (Comppostqx = "IV" AND Tokyo = "Leve") OR (Comppostqx = "V" AND Tokyo= "Leve")')
    tokyo_morb_alta=cur.fetchone() 
    
    p_tokyo_leve='?'  
    
    #tokyo moderado
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Moderado") OR (Comppostqx = "II" AND Tokyo = "Moderado")')
    tokyoII_morb_baja=cur.fetchone()
    
    #tokyo moderado morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Moderado") OR (Comppostqx = "IV" AND Tokyo = "Moderado") OR (Comppostqx = "V" AND Tokyo= "Moderado")')
    tokyoII_morb_alta=cur.fetchone() 
    
    p_tokyo_moderado='?'  
    
    #tokyo severo
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Severo") OR (Comppostqx = "II" AND Tokyo = "Severo")')
    tokyoIII_morb_baja=cur.fetchone()
    
    #tokyo moderado morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Severo") OR (Comppostqx = "IV" AND Tokyo = "Severo") OR (Comppostqx = "V" AND Tokyo= "Severo")')
    tokyoIII_morb_alta=cur.fetchone() 
    
    p_tokyo_severo='0.16'  
    
    index_tokyo=['Tokyo I','Tokyo II','Tokyo III'] 
    column_tokyo=['CD I y II','CD >III','p']
    data_tokyo=[(tokyo_morb_baja,tokyo_morb_alta,p_tokyo_leve),
                (tokyoII_morb_baja,tokyoII_morb_alta,p_tokyo_moderado),
                (tokyoIII_morb_baja,tokyoIII_morb_alta,p_tokyo_severo)]
    tokyo_df=pd.DataFrame(data_tokyo,index_tokyo,column_tokyo)
    st.dataframe(tokyo_df)

def motivo():
    st.info('Motivo de ingreso, análisis ordinal')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #Patología vesicular de inicio
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%[]%" AND Comppostqx="I")  OR (PRoccardio LIKE "%[]%" AND Comppostqx="II")' )
    colnomor_res=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%[]%"AND Comppostqx="III") OR (PRoccardio LIKE "%[]%"AND Comppostqx="IV") OR (PRoccardio LIKE "%[]%"AND Comppostqx="V")' )
    colsimor_res=cur.fetchone()
    
    
    #infarto agudo al miocardio con morbilidad baja
    iam_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Infarto%" OR PRoccardio LIKE "%Cateterismo%") AND (Comppostqx="I" OR Comppostqx="II")' )
    iamnomor_res=cur.fetchone()
    
    iam_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Infarto%" OR PRoccardio LIKE "%Cateterismo%") AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")' )
    iammorta_res=cur.fetchone()
    
    
     #Arritmia
    arritmia_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%marcapaso%" ) AND (Comppostqx="I" OR Comppostqx="II")' )
    arritmia_nomor_res=cur.fetchone()
    
    arritmia_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%marcapaso%") AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")' )
    arritmia_morta_res=cur.fetchone()
    
    
    
    #Cirugía
    cirugía_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Cirugia%" OR PRoccardio Like "%Reemplazo%") AND (Comppostqx="I" OR Comppostqx="II")' )
    cx_nomor_res=cur.fetchone()
    
    cx_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Cirugia%" OR PRoccardio Like "%Reemplazo%") AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")' )
    cx_morta_res=cur.fetchone()
    
    
    #ICC
    IC_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%funcional%" ) AND (Comppostqx="I" OR Comppostqx="II")' )
    IC_nomor_res=cur.fetchone()
    
    
    IC_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%funcional%" ) AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")' )
    IC_morta_res=cur.fetchone()
    
    #Dataframe
    data=[(colnomor_res,colnomor_res/18,colsimor_res,colsimor_res/18),
          (iamnomor_res,iamnomor_res/18,iammorta_res,iammorta_res/18),
          (arritmia_nomor_res,arritmia_nomor_res/18,arritmia_morta_res,arritmia_morta_res/18),
          (cx_nomor_res,cx_nomor_res/18,cx_morta_res,cx_morta_res/18),
          (IC_nomor_res,IC_nomor_res/18,IC_morta_res,IC_morta_res/18)]
    index_motiv=['CCLA','IAM','Arritmia','Cirugía cardiovascular','ICC']
    column_motiv=['CD I y II','%','CD>III','%%']
    motiv_df=pd.DataFrame(data,index_motiv,column_motiv)
    st.dataframe(motiv_df)
    hu=np.array([[36.6,63.4],[41.7,58.3]])
    re=stats.fisher_exact(hu)
    st.write(re)
    
    
def hallazgos_mort():
    st.info('Hallazgos transquirúrgicos y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #Distensión
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Distensión%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_distensión_baja=cur.fetchone()
    
    porc_distension_baja=hall_distensión_baja/18
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Distensión%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_distensión_alta=cur.fetchone()
    
    porc_distension_alta=hall_distensión_alta/18
    tabla=[5,4],[6,3]
    o,p_distensión,=stats.fisher_exact(tabla)
    
    #Necrosis
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%necrosis vesicular%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_necrosisves_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%necrosis vesicular%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_necrosisves_alta=cur.fetchone()
    
    tabla_necro=[4,6],[7,1]
    o,y_distensión,=stats.fisher_exact(tabla_necro)
    
    
    #NEcrosis cístico
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Necrosis de cístico%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_necrosiscist_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Necrosis de cístico%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_necrosiscist_alta=cur.fetchone()
    
    tabla_necrocist=[hall_necrosiscist_baja,10],[hall_necrosiscist_alta,6]
    h,p_necrocist=stats.fisher_exact(tabla_necrocist)
    
    
    #Líquido perivesicular
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Líquido perivesicular%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_liqperives_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Líquido perivesicular%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_liqperives_alta=cur.fetchone()
    
    u,p_liq=stats.fisher_exact(([2,1],[9,6]))
    
    
    #Piocolecisto
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Piocolecisto%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_piocolecisto_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Piocolecisto%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_piocolecisto_alta=cur.fetchone()
    
    ug,p_pio=stats.fisher_exact(([7,3],[4,4]))
    
    
    
    
    #Engrosamiento de pared
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Engrosamiento%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_engrosamiento_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Engrosamiento%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_engrosamiento_alta=cur.fetchone()
    
    ugr,p_engrosamiento=stats.fisher_exact(([6,2],[5,5]))
    
    
    
     #Perforación vesicular
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Perforación%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_perforación_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%perforación%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_perforación_alta=cur.fetchone()
    
    uggg,p_perforación=stats.fisher_exact(([1,3],[10,4]))
    
    
    
     #abscesco peri vesicular
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Absceso%" AND (Comppostqx="I" OR Comppostqx="II")')
    hall_absceso_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Absceso%" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    hall_absceso_alta=cur.fetchone()
    
    ugggee,p_absceso=stats.fisher_exact(([1,0],[10,7]))
    
    data_hallzgos=[(hall_distensión_baja,hall_distensión_alta,p_distensión),(hall_necrosisves_baja,hall_necrosisves_alta,y_distensión),
                   (hall_necrosiscist_baja,hall_necrosiscist_baja,p_necrocist),
                   (hall_liqperives_baja,hall_liqperives_alta,p_liq),
                   (hall_piocolecisto_baja,hall_piocolecisto_alta,p_pio),
                   (hall_engrosamiento_baja,hall_engrosamiento_alta,p_engrosamiento),
                   (hall_perforación_baja,hall_perforación_alta,p_perforación),
                   (hall_absceso_baja,hall_absceso_alta,p_absceso)]
    index_hallazgos=['Distensión vesicular','Necrosis vesicular','Necrosis cístico','Líquido perivesicular',
                     'Piocolecisto','Pared engrosada','Perforación vesicular','Absceso perivesicular']
    col_hallzgos=['CD I y II','CD >III','p']
    df_hallazgos=pd.DataFrame(data_hallzgos,index_hallazgos,col_hallzgos)
    st.dataframe(df_hallazgos)
    
    
def tokyo_no_trend():
    st.info('Análisis no trend de ASA y Tokyo vs morbimorta')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
     #tokyo leve
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Leve") OR (Comppostqx = "II" AND Tokyo = "Leve")')
    tokyo_morb_baja=cur.fetchone()
    
    #tokyo leve morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Leve") OR (Comppostqx = "IV" AND Tokyo = "Leve") OR (Comppostqx = "V" AND Tokyo= "Leve")')
    tokyo_morb_alta=cur.fetchone() 
    
    z,p_tokyo_leve,=stats.fisher_exact(([tokyo_morb_baja,tokyo_morb_alta],[7,6])) 
    
    
    #tokyo mod
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Moderado") OR (Comppostqx = "II" AND Tokyo = "Moderado")')
    tokyo_mode_baja=cur.fetchone()
    
    #tokyo leve morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Moderado") OR (Comppostqx = "IV" AND Tokyo = "Moderado") OR (Comppostqx = "V" AND Tokyo= "Moderado")')
    tokyo_mode_alta=cur.fetchone() 
    
    zi,tokyomod_p,=stats.fisher_exact(([tokyo_mode_baja,tokyo_mode_alta],[7,1])) 
    
    
    
     #tokyo sev
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "I" AND Tokyo = "Severo") OR (Comppostqx = "II" AND Tokyo = "Severo")')
    tokyo_sev_baja=cur.fetchone()
    
    #tokyo leve morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (Comppostqx = "III" AND Tokyo = "Severo") OR (Comppostqx = "IV" AND Tokyo = "Severo") OR (Comppostqx = "V" AND Tokyo= "Severo")')
    tokyo_sev_alta=cur.fetchone() 
    
    zi,tokyosev_p,=stats.fisher_exact(([tokyo_sev_baja,tokyo_sev_alta],[4,7])) 
    
    data_tokyo=[(tokyo_morb_baja,tokyo_morb_alta,p_tokyo_leve),
                (tokyo_mode_baja,tokyo_mode_alta,tokyomod_p),
                (tokyo_sev_baja,tokyo_sev_alta,tokyosev_p)]
    indextokyo=['Tokyo I','Tokyo II','Tokyo III']
    col_tokyo=['CD I y II','CD>III','p']
    df_tokyo=pd.DataFrame(data_tokyo,indextokyo,col_tokyo)
    st.dataframe(df_tokyo)
    
def asa_notrend():
    st.info('ASA no trend')
    #ASA
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #ASA I es cero no tenemos pacientes
    #ASAII
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="I" ) OR (asa="II" AND Comppostqx= "II" )')
    asaII_baja=cur.fetchone()
        
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="III" ) OR (asa="II" AND Comppostqx= "IV" )OR (asa="II" AND Comppostqx= "V" )')
    asaII_alta=cur.fetchone()
    
    gu,p_asaII=stats.fisher_exact(([asaII_baja,asaII_alta],[9,7]))
    
    
    #ASAIII
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="I" ) OR (asa="III" AND Comppostqx= "II" )')
    asaIII_baja=cur.fetchone()
        
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="III" ) OR (asa="III" AND Comppostqx= "IV" )OR (asa="III" AND Comppostqx= "V" )')
    asaIII_alta=cur.fetchone()
    
    gug,p_asaIII=stats.fisher_exact(([asaIII_baja,asaIII_alta],[8,6]))
    
    
    #ASAIV
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="I" ) OR (asa="IV" AND Comppostqx= "II" )')
    asaIV_baja=cur.fetchone()
        
    cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="III" ) OR (asa="IV" AND Comppostqx= "IV" )OR (asa="IV" AND Comppostqx= "V" )')
    asaIV_alta=cur.fetchone()
    
    guge,p_asaIV=stats.fisher_exact(([asaIV_baja,asaIV_alta],[5,1]))
    
    data_asa=[(asaII_baja,asaII_alta,p_asaII),
              (asaIII_baja,asaIII_alta,p_asaIII),
              (asaIV_baja,asaIV_alta,p_asaIV)]
    index_asa=['ASA II','ASA III','ASA IV']
    col_asa=['CD I y II','CD >III','p']
    df_asa=pd.DataFrame(data_asa,index_asa,col_asa)
    st.dataframe(df_asa)
    
    

    
def tablano8():
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    st.info('Laboratorios prequirúrgicos')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #ADE preqx vs morbimorta
    cur.execute('SELECT ADEpreqx From Basecxcol WHERE ADEpreqx != 0 AND (Comppostqx="I" OR Comppostqx="II")')
    adepreqx_baja=cur.fetchall()
    adepreqx_baja_avg=np.average(adepreqx_baja)
    
    #ADE preqx vs morbimorta
    cur.execute('SELECT ADEpreqx From Basecxcol WHERE ADEpreqx != 0 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    adepreqx_alta=cur.fetchall()
    adepreqx_alta_avg=np.average(adepreqx_alta)
    
    i,p_ade=stats.ttest_ind(adepreqx_baja,adepreqx_alta,equal_var=False)
    
    #DF
    data_preqx=[(adepreqx_baja,adepreqx_baja_avg,adepreqx_alta,adepreqx_alta_avg,p_ade)]
    index_preqx=['ADE']
    Col_preqx=['ADE baja','ADE prom baja','ADE alta','ADE prom alta','p']
    df_preqx=pd.DataFrame(data_preqx,index_preqx,Col_preqx)
    st.dataframe(df_preqx)
    
    
def tabla_extras():
    st.info('Extras')
    #Genero, edad, BMI, tabaquismo
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Género="Masculino" AND (Comppostqx="I" OR Comppostqx="II")')
    masculino_baja=cur.fetchone()
    
    #genero masculino morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Género="Masculino" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    masculino_alta=cur.fetchone()
    
    #genero femenino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Género="Femenino" AND (Comppostqx="I" OR Comppostqx="II")')
    femenino_baja=cur.fetchone()
    
    #genero femenino morb alta
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Género="Femenino" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    femenino_alta=cur.fetchone()
    
    j,p_genero=stats.fisher_exact(([5,5],[6,2]))
    
    
    index_genero=['Hombre','Mujer']
    col_genero=['CD I y II','CD >III','p']
    df_genero=pd.DataFrame([(masculino_baja,masculino_alta,p_genero),
                            (femenino_baja,femenino_alta)],index_genero,col_genero)
    st.dataframe(df_genero)
    
    
    #Edad morb baja
    cur.execute('SELECT Edad From Basecxcol WHERE Edad!=0 AND (Comppostqx="I" OR Comppostqx="II")')
    edad_baja=cur.fetchall()
    edad_baja_avg=np.average(edad_baja)
    
    #Edad morb alta
    cur.execute('SELECT Edad From Basecxcol WHERE Edad!=0 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    edad_alta=cur.fetchall()
    edad_alta_avg=np.average(edad_alta)
    
    x,p_edad=stats.ttest_ind(edad_baja,edad_alta)
    
    data_edad=[(edad_baja,edad_baja_avg,edad_alta,edad_alta_avg,p_edad)]
    index_edad=['Edad']
    col_edad=['CD I y II','Prom', 'CD > III','Promedio','p']
    #Df
    df_edad=pd.DataFrame(data_edad,index_edad,col_edad)
    st.dataframe(df_edad)
    
    
    #BMI morb baja
    cur.execute('SELECT IMC From Basecxcol WHERE IMC!=0 AND (Comppostqx="I" OR Comppostqx="II")')
    IMC_baja=cur.fetchall()
    IMC_baja_avg=np.average(IMC_baja)
    
    #BMI morb alta
    cur.execute('SELECT IMC From Basecxcol WHERE IMC!=0 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    IMC_alta=cur.fetchall()
    IMC_alta_avg=np.average(IMC_alta)
    
    xx,p_IMC=stats.ttest_ind(IMC_baja,IMC_alta)
    
    data_IMC=[(IMC_baja,IMC_baja_avg,IMC_alta,IMC_alta_avg,p_IMC)]
    index_IMC=['IMC']
    col_IMC=['CD I y II','Prom', 'CD > III','Promedio','p']
    #Df
    df_IMC=pd.DataFrame(data_IMC,index_IMC,col_IMC)
    st.dataframe(df_IMC)
    
def ventilacionmec():
    st.info('Ventilación mecanica y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Diasventmec!=0 AND (Comppostqx="I" OR Comppostqx="II")')
    ventmec_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Diasventmec!=0 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    ventmec_alta=cur.fetchone()
    
    yu,p_ventmec,=stats.fisher_exact(([ventmec_baja,ventmec_alta],[9,2]))
    #df
    index_ventmec=['Ventilación mecánica']
    col_ventmec=['CD I y II', 'CD>III','p']
    data_ventmec=[(ventmec_baja,ventmec_alta,p_ventmec)]
    st.dataframe(pd.DataFrame(data_ventmec,index_ventmec,col_ventmec))
    
    
def tabaquismo():
    st.info('Tabaquismo y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo="Si" AND (Comppostqx="I" OR Comppostqx="II")')
    tab_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo="Si" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    tab_alta=cur.fetchone()
    
    yu,p_tab,=stats.fisher_exact(([tab_baja,tab_alta],[7,2]))
    #df
    index_tab=['Tabaquismo ']
    col_tab=['CD I y II', 'CD>III','p']
    data_tab=[(tab_baja,tab_alta,p_tab)]
    st.dataframe(pd.DataFrame(data_tab,index_tab,col_tab))
    
def vasopresposqx():
    st.info('Vasopresor postqx y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE postqxvasopresor="Si" AND (Comppostqx="I" OR Comppostqx="II")')
    vasopresposqx_baja=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE postqxvasopresor="Si" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    vasopresorposqx_alta=cur.fetchone()
    
    yu,p_vasopres,=stats.fisher_exact(([vasopresposqx_baja,vasopresorposqx_alta],[9,1]))
    #df
    index_vasopres=['Vasopresor posquirúrgico ']
    col_vasopres=['CD I y II', 'CD>III','p']
    data_vasopres=[(vasopresposqx_baja,vasopresorposqx_alta,p_vasopres)]
    st.dataframe(pd.DataFrame(data_vasopres,index_vasopres,col_vasopres))
    
    
def pade_sint():
    st.info('Duración de cirugía y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Tiempoinsintqx!=1 AND (Comppostqx="I" OR Comppostqx="II")')
    duraciónqx_baja=cur.fetchall()
    st.write(duraciónqx_baja)
    ave_duracion_baja=np.average(duraciónqx_baja)
    
    t,shapiro_duracionbaja=stats.shapiro(duraciónqx_baja)
    st.write(shapiro_duracionbaja)
    
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Tiempoinsintqx!=1 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    duraciónqx_alta=cur.fetchall()
    st.write(duraciónqx_alta)
    aveg_duracion_alta=np.average(duraciónqx_alta)
    data_tt=np.array(duraciónqx_baja)
    dta_bb=np.array(duraciónqx_alta)
    yu,p_duracionqx,=stats.mannwhitneyu(data_tt,dta_bb)
    #df
    index_duracion=['Duración cirugía ']
    col_duracion=['CD I y II', 'CD>III','p']
    data_duracion=[(ave_duracion_baja,aveg_duracion_alta,p_duracionqx)]
    st.dataframe(pd.DataFrame(data_duracion,index_duracion,col_duracion))
    st.write(duraciónqx_baja)

    
    
def padecimiento_dias():
    st.info('Padecimiento actual y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    Tiempoinsintqx_baja=cur.fetchall()
    st.write(Tiempoinsintqx_baja)
    ave_tiempoinsintqx_baja=np.average(Tiempoinsintqx_baja)
    
    t,shapiro__tiempoinsintqxbaja=stats.shapiro(Tiempoinsintqx_baja)
    st.write(Tiempoinsintqx_baja)
    
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V"')
    Tiempoinsintqx_alta=cur.fetchall()
    st.write(Tiempoinsintqx_alta)
    aveg_duracion_alta=np.average(Tiempoinsintqx_alta)
    data_tt=np.array(Tiempoinsintqx_baja)
    dta_bb=np.array(Tiempoinsintqx_alta)
    yu,p_tiempoinsintqx,=stats.mannwhitneyu(data_tt,dta_bb)
    #df
    index_duracion=['Tiempo de inicio de padecimiento actual']
    col_duracion=['CD I y II', 'CD>III','p']
    data_duracion=[(ave_tiempoinsintqx_baja,aveg_duracion_alta,p_tiempoinsintqx)]
    st.dataframe(pd.DataFrame(data_duracion,index_duracion,col_duracion))
    st.write(Tiempoinsintqx_baja)


def vasopresores_preqx():
    st.info('Vasopresor prequirúrgico y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores="Si" AND (Comppostqx="I" OR Comppostqx="II")')
    Vasopresores_baja=cur.fetchall()
    st.write(Vasopresores_baja)
    ave_Vasopresores_baja=np.average(Vasopresores_baja)
    
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores="Si" AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    Vasopresores_alta=cur.fetchall()
    aveg_duracion_alta=np.average(Vasopresores_alta)
    data_tt=np.array(Vasopresores_baja)
    dta_bb=np.array(Vasopresores_alta)
    yu,p_vasopresores,= stats.fisher_exact(([4,3],[7,3]))
    #df
    index_duracion=['Uso de vasopresores prequirúrgicos']
    col_duracion=['CD I y II', 'CD>III','p']
    data_duracion=[(ave_Vasopresores_baja,aveg_duracion_alta,p_vasopresores)]
    st.dataframe(pd.DataFrame(data_duracion,index_duracion,col_duracion))
    st.write(Vasopresores_baja)


def edad_60omas():
    st.info('60 o mas años y morbimortalidad')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #genero masculino morb baja
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Edad>=60 AND (Comppostqx="I" OR Comppostqx="II")')
    edad_baja=cur.fetchall()
    
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Edad>=60 AND (Comppostqx="III" OR Comppostqx="IV" OR Comppostqx="V")')
    edad_alta=cur.fetchall()
    yu,p_vasopresores,= stats.fisher_exact(([8,7],[3,0]))
    #df
    index_duracion=['Edad >60']
    col_duracion=['CD I y II', 'CD>III','p']
    data_duracion=[(edad_baja,edad_alta,p_vasopresores)]
    st.dataframe(pd.DataFrame(data_duracion,index_duracion,col_duracion))



def tabla_comparativa_ingpreqx():
    st.info('Comparativa de variables ingreso vs prequirúrgicas')
    
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    
    #FC
    cur.execute('SELECT FCing FROM Basecxcol  WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    fcing_av=cur.fetchall()
    fcing_average=np.average(fcing_av)
    st.success(fcing_average)
    
    cur.execute('SELECT FCpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    fc_preqx_avg=cur.fetchall()
    fcpreqx_average=np.average(fc_preqx_avg)
    
    i,p_fc=stats.ttest_rel(fcing_av,fc_preqx_avg)
    st.write(p_fc)
    
    
    #FR
    cur.execute('SELECT FRing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    fr_ing=cur.fetchall()
    fr_average=np.average(fr_ing)
   
    
    cur.execute('SELECT FRpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    fr_preqx=cur.fetchall()
    frpreqx_average=np.average(fr_preqx)
    
    di,p_fr=stats.ttest_rel(fr_ing,fr_preqx)
    st.write(p_fr)

    
    
    #Sistólica
    cur.execute('SELECT Sising FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    sis_ing_avg=cur.fetchall()
    sis_average=np.average(sis_ing_avg)
    
    cur.execute('SELECT Sistpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')  
    sis_preqx_avg=cur.fetchall()
    sispreqx_average=np.average(sis_preqx_avg)
    
    dief,p_sis=stats.ttest_rel(sis_ing_avg,sis_preqx_avg)
    st.write(p_sis)
    
    
    #Diastólica
    cur.execute('SELECT Diasing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    diasting_avg=cur.fetchall()
    diasting_average=np.average(diasting_avg)
    
    cur.execute('SELECT Diastpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    diast_preqx_avg=cur.fetchall()
    diastpreqx_average=np.average(diast_preqx_avg)
    
    diefe,p_dias=stats.ttest_rel(diasting_avg,diast_preqx_avg)
    st.write(p_dias)
    
    
    #Temp
    cur.execute('SELECT Temping FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    temp_ing_avg=cur.fetchall()
    temp_average=np.average(temp_ing_avg)
    
    cur.execute('SELECT Temppreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    temp_preqx=cur.fetchall()
    temppreqx_average=np.average(temp_preqx)
    
    diefee,p_temp=stats.ttest_rel(temp_ing_avg,temp_preqx)
    st.write(p_temp)
    
    
    #Leu
    cur.execute('SELECT Leuing FROM Basecxcol WHERE Leuing !=1 AND (Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III")') 
    leu_ing_avg=cur.fetchall()
    st.write(leu_ing_avg)
    
    cur.execute('SELECT Leupreqx FROM Basecxcol WHERE Leupreqx!=1 AND (Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III")') 
    leu_preqx=cur.fetchall()
    st.write(leu_preqx)
    #los arrays son diferentes por el 1 en el ultimo paciente que tiene leucos de 1 en ingreso y 11 de preqx, se va a quitar y se hcen los arrays manuales
    
    a=[6,15,14,5,22,15]
    leuing_average=np.average(a)
    b=[17,10,18,14,22,23]
    
    leupreqx_average=np.average(b)
    fer,p_leu=stats.ttest_rel(a,b)
    
    
    #HTO
    cur.execute('SELECT Hematocritoing FROM Basecxcol WHERE Hematocritoing!=1 AND (Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III")') 
    hto_ing_avg=cur.fetchall()
    st.error(hto_ing_avg)
    
    cur.execute('SELECT HTOpreqx FROM Basecxcol WHERE  HTOpreqx!=1 AND (Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III")') 
    hto_preqx=cur.fetchall()
    st.warning(hto_preqx)
    
    #Igual tenian arrays de diferente tamaño se hizo la comparativa manual
    c=[38, 46, 35, 33, 50, 50]
    htoing_average=np.average(c)
    d=[37, 43, 27, 31, 50, 47]
    hto_preqx_average=np.average(d)
    fder,p_hto=stats.ttest_rel(c,d)
    st.write(p_hto)

     
    
    #ADE hay uno de los pacientes que no tiene ADE así que se hizo manual el Array
    e=[13,12,13,22,15,13]
    f=[ 13,12,16,20,15,13]
    cur.execute('SELECT ADEing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    ade_ing_avg=e
    
    cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    ade_preqx=f
    

    
    adepreqx_average=np.average(f)
    adeing_average=np.average(e)
    fdere,p_ADE=stats.ttest_rel(e,f)
    st.write(p_ADE)
    
    
    
    #plaq tampoco tenemos un dato asi que se removió para la comparativa y el array se hizo manual
    h=[102,257,248,183,176,202]
    i=[106,360,668,106,176,223]
    
    cur.execute('SELECT Plaquetasing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    plaq_ing_avg=h
    
    cur.execute('SELECT Plaqpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    plaq_preqx=i
    
    
    plaqing_average=np.average(h)
    plaqpreqx_average=np.average(i)


    
    fdere,p_plaq=stats.ttest_rel(h,i)
    st.write(p_plaq)
   
    #AST
    cur.execute('SELECT ASTing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    ast_ing_avg=cur.fetchall()
    asting_average=np.average(ast_ing_avg)
    
    cur.execute('SELECT ASTpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    ast_preqx=cur.fetchall()
    astpreqx_average=np.average(ast_preqx)
    
    fdere,p_AST=stats.ttest_rel(ast_ing_avg,ast_preqx)
    st.write(p_AST)
    
    
    #ALT
    cur.execute('SELECT ALTing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    alt_ing_avg=cur.fetchall()
    alting_average=np.average(alt_ing_avg)
    
    cur.execute('SELECT ALTpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    alt_preqx=cur.fetchall()
    altpreqx_average=np.average(alt_preqx)
    
    fder,p_alt=stats.ttest_rel(alt_ing_avg,alt_preqx)
    st.write(p_alt)
    
    
     #Bil los arrays estaban incompletos se eliminarion los valores 1 y 0
     
    j=[2.65,0.87,1.08,0.87]
    k=[3.03,1.17,1.08,1.23]
    cur.execute('SELECT Biltoting FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    bil_ing_avg=j
    
    cur.execute('SELECT Biltotpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    bil_preqx=k
    
   
    biling_average=np.average(j)

    bilpreqx_average=np.average(k)

    
    fdeeer,p_bil=stats.ttest_rel(j,k)
    st.write(p_bil)
    
    
         #INR
    cur.execute('SELECT INRing FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    INR_ing_avg=cur.fetchall()
    INRing_average=np.average(INR_ing_avg)
    
    cur.execute('SELECT INRpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    INR_preqx=cur.fetchall()
    INRpreqx_average=np.average(INR_preqx)
    
    fder,p_INR=stats.ttest_rel(INR_ing_avg,INR_preqx)
    st.write(p_INR)
    
    
        #Creatinina arrays incompletos se realizo manual
        
    k=[1.07,1.53,0.96,1.1,]
    l=[0.98,1.81,0.96,1.37]
    cur.execute('SELECT Creating FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    Creat_ing_avg=k
    creaing_average=np.average(Creat_ing_avg)
    
    cur.execute('SELECT Creatpreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    Creat_preqx=l
    creatpreqx_average=np.average(Creat_preqx)
    
    fder,p_Creat=stats.ttest_rel(Creat_ing_avg,Creat_preqx)
    st.write(p_Creat)
    
   
      #qSOFA
    cur.execute('SELECT qSOFA FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    qsofa_ing_avg=cur.fetchall()
    qsofaing_average=np.average(qsofa_ing_avg)
    
    cur.execute('SELECT qSOFApreqx FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"') 
    qsofa_preqx=cur.fetchall()
    qsofapreqx_average=np.average(qsofa_preqx)
    
    fder,p_qSOFA=stats.ttest_rel(qsofa_ing_avg,qsofa_preqx)
    st.write(p_qSOFA)
    
    
    
    
    data_comp=[(fcing_av,fcing_average,fc_preqx_avg,fcpreqx_average,p_fc),(fr_ing,fr_average,fr_preqx,frpreqx_average,p_fr),
               (sis_ing_avg,sis_average,sis_preqx_avg,sispreqx_average,p_sis),(diasting_avg,diasting_average,diast_preqx_avg,diastpreqx_average,p_dias),
               (temp_ing_avg,temp_average,temp_preqx,temppreqx_average,p_temp),(leu_ing_avg,leuing_average,leu_preqx,leupreqx_average,p_leu),
               (hto_ing_avg,htoing_average,hto_preqx,hto_preqx_average,p_hto),(ade_ing_avg,adeing_average,ade_preqx,adepreqx_average,p_ADE),
               (plaq_ing_avg,plaqing_average,plaq_preqx,plaqpreqx_average,p_plaq),(ast_ing_avg,asting_average,ast_preqx,astpreqx_average,p_AST),
               (alt_ing_avg,alting_average,alt_preqx,altpreqx_average,p_alt),(bil_ing_avg,biling_average,bil_preqx,bilpreqx_average,p_bil),
               (INR_ing_avg,INRing_average,INR_preqx,INRpreqx_average,p_INR),(Creat_ing_avg,creaing_average,Creat_preqx,creatpreqx_average,p_Creat),
               (qsofa_ing_avg,qsofaing_average,qsofa_preqx,qsofapreqx_average,p_qSOFA)]
    data_comp_index=['Frecuencia cardiáca/min *','Frecuencia respiratoria/min CD<III','Presión sistólica mmHg CD<III','Presión diastólica mmHg CD>III ',
                     'Temperatura °C CD >III','Leucocitos mm3 CD>III','Hematocrito CD>III',
                     'ADE CD>III','Plaquetas mm3 CD>III','AST mg/dl CD>III','ALT mg/dl CD>III',
                     'Bilirrubina total mg/dl CD>III','INR CD>III','Creatinina (mg/dl) CD>III',
                     'qSOFA CD>III']
    data_comp_columns=['Ingreso','Promedio','Prequirúrgica','Promedio 2','p']
    df_comparacion=pd.DataFrame(data_comp,index=data_comp_index,columns=data_comp_columns)
    dfcomp_arevs=df_comparacion.T
    st.dataframe(df_comparacion )
    
    #Seleccionar los  labs de ingreso y prequirúrgicos de los pacients con morbi-morta elevados en una fila
    #Seleciconar los labs de ingreso y prequirúrgicos de los pacientes con morbi-morta bajos en otra fila
    
    # en el articulo de laurila comparan el SOFA en admisión entre dos grupos (muertos vs vivos) y luego prequirúrgico
    #entre muertos y vivos
    
    
    
    
    
def imagen():
    st.info('Estudios de imagen')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
    #Hallazgos por ultrasonido
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%perivesicular%"')
    usg_liqperi=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Engrosamiento%"')
    usg_engros=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Distensión%"')
    usg_diste=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Litiasis%"')
    usg_lit=cur.fetchone()
    st.write(usg_lit)
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Lodo%"')
    usg_Lodo=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Dilatación%"')
    usg_dil=cur.fetchone()
    
    #Hallazgos TAC
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Estriación%"')
    tac_estriacion=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Hidrocolecisto%" OR Hallazgtom LIKE "%Distensión%" ')
    tac_hidro=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Líquido%"')
    tac_líquido=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Engrosamiento%"')
    tac_engrosamiento=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Litiasis%"')
    tac_litiasis=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Reforzamiento%"')
    tac_reforz=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgtom LIKE "%Lito%"')
    tac_litobil=cur.fetchone()
    
    data_imagen=[usg_liqperi,usg_engros,usg_lit,usg_Lodo,usg_dil,tac_estriacion,tac_hidro,tac_líquido,tac_engrosamiento,tac_litiasis,tac_reforz,tac_litobil]
    index_imagen=['Líquido perivesicular','Engrosamiento de pared','Litiasis vesicular','Lodo vesicular','Hidrocolecisto',
                  'Estriación de grasa perivesicular (TC)','Hidrocolecisto(TC)','Líquido perivesicular(TC)',
                  'Engrosamiento de pared(TC)','Litiasis vesicular(TC)','Captación de contraste vesicular(TC)','Lito en via biliar(TC)']
    col_imagen=['Hallazgos']
    df_imagen=pd.DataFrame(data_imagen,index_imagen,col_imagen)
    st.dataframe(df_imagen,width=800)
    
    

def kruskallwallis():
    st.error('Test Kruskall-wallis')
    con=sqlite3.connect('DB.db')
    con.row_factory = lambda cursor, row: row[0]
    cur=con.cursor()
   
    #Leucocitosis
    cur.execute('SELECT Leupreqx FROM Basecxcol WHERE Leupreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    Leu_I_II=cur.fetchall()
    
    avg_leuI_II=np.average(Leu_I_II)
    
    x,shap_LeuI=stats.shapiro(Leu_I_II)
    
    cur.execute('SELECT Leupreqx FROM Basecxcol WHERE Leupreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    Leu_III_IV=cur.fetchall()
    
    avg_leuIII_IV=np.average(Leu_III_IV)
    
    shap_III_IV='stats.shapiro(Leu_III_IV)'
    
    cur.execute('SELECT Leupreqx FROM Basecxcol WHERE Leupreqx!=0 AND Comppostqx ="V"')
    Leu_V=cur.fetchall()
    
    avg_leuV=np.average(Leu_V)
    
    k,shap_V=stats.shapiro(Leu_V)

    h,kruskal_leu=stats.kruskal(Leu_I_II,Leu_III_IV,Leu_V)
   #termina leucocitos
   
   #ADE
   
   #ADE I y II
    cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE ADEpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    ADE_I_II=cur.fetchall()
    
    avg_ADEI_II=np.average(ADE_I_II)
    
    x,shap_ADEI=stats.shapiro(ADE_I_II)
    
     #ADE III y IV
    cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE ADEpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    ADE_III_IV=cur.fetchall()
    
    avg_ADEIII_IV=np.average(ADE_III_IV)
    
    shap_ADEIII_IV='stats.shapiro(ADE_III_IV)'
    
    #ADE V
    cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE ADEpreqx!=0 AND Comppostqx ="V" ')
    ADE_V=cur.fetchall()
    
    avg_ADE_V=np.average(ADE_V)
    
    l,shap_ADE_V=stats.shapiro(ADE_V)
   
    o,kruskal_ade=stats.kruskal(ADE_I_II,ADE_III_IV,ADE_V)
    
    
    #HTO
    #ADE I y II
    cur.execute('SELECT HTOpreqx FROM Basecxcol WHERE HTOpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    HTO_I=cur.fetchall()
    
    avg_HTOI=np.average(HTO_I)
    
    u,shap_HTOI=stats.shapiro(HTO_I)
    
    #HTO III
    cur.execute('SELECT HTOpreqx FROM Basecxcol WHERE HTOpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    HTOIII=cur.fetchall()
    
    avg_HTOIII_IV=np.average(HTOIII)
    
    'shap_HTOIII=stats.shapiro(HTOIII)'
    
     #HTO V
    cur.execute('SELECT HTOpreqx FROM Basecxcol WHERE HTOpreqx!=0 AND Comppostqx ="V" ')
    HTO_V=cur.fetchall()
    
    avg_HTO_V=np.average(HTO_V)
    
    t,shap_HTO_V=stats.shapiro(HTO_V)
   
    i,kruskal_HTO=stats.kruskal(HTO_I,HTOIII,HTO_V)
   
    
    #Plaquetas
    #Plaq
    cur.execute('SELECT Plaqpreqx FROM Basecxcol WHERE Plaqpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    Plaq_I=cur.fetchall()
    
    avg_PlaqI=np.average(Plaq_I)
    
    u,shap_PlaqI=stats.shapiro(Plaq_I)
    
    #Plaq III
    cur.execute('SELECT Plaqpreqx FROM Basecxcol WHERE Plaqpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    PlaqIII=cur.fetchall()
    
    avg_PlaqIII_IV=np.average(PlaqIII)
    
    'shap_PlaqIII=stats.shapiro(PlaqIII)'
    
     #Plaq V
    cur.execute('SELECT Plaqpreqx FROM Basecxcol WHERE Plaqpreqx!=0 AND Comppostqx ="V" ')
    Plaq_V=cur.fetchall()
    
    avg_Plaq_V=np.average(Plaq_V)
    
    t,shap_Plaq_V=stats.shapiro(Plaq_V)
   
    i,kruskal_Plaq=stats.kruskal(Plaq_I,PlaqIII,Plaq_V)
    
    #AST
    #AST
    cur.execute('SELECT ASTpreqx FROM Basecxcol WHERE ASTpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    AST_I=cur.fetchall()
    
    avg_ASTI=np.average(AST_I)
    
    u,shap_ASTI=stats.shapiro(AST_I)
    
    #AST III
    cur.execute('SELECT ASTpreqx FROM Basecxcol WHERE ASTpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    ASTIII=cur.fetchall()
    
    avg_ASTIII_IV=np.average(ASTIII)
    
    'shap_ASTIII=stats.shapiro(ASTIII)'
    
     #AST V
    cur.execute('SELECT ASTpreqx FROM Basecxcol WHERE ASTpreqx!=0 AND Comppostqx ="V" ')
    AST_V=cur.fetchall()
    
    avg_AST_V=np.average(AST_V)
    
    t,shap_AST_V=stats.shapiro(AST_V)
   
    i,kruskal_AST=stats.kruskal(AST_I,ASTIII,AST_V)
   
    #ALT
    
    #ALT
    cur.execute('SELECT ALTpreqx FROM Basecxcol WHERE ALTpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    ALT_I=cur.fetchall()
    
    avg_ALTI=np.average(ALT_I)
    
    u,shap_ALTI=stats.shapiro(ALT_I)
    
    #ALT III
    cur.execute('SELECT ALTpreqx FROM Basecxcol WHERE ALTpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    ALTIII=cur.fetchall()
    
    avg_ALTIII_IV=np.average(ALTIII)
    
    'shap_ALTIII=stats.shapiro(ALTIII)'
    
     #ALT V
    cur.execute('SELECT ALTpreqx FROM Basecxcol WHERE ALTpreqx!=0 AND Comppostqx ="V" ')
    ALT_V=cur.fetchall()
    
    avg_ALT_V=np.average(ALT_V)
    
    t,shap_ALT_V=stats.shapiro(ALT_V)
   
    i,kruskal_ALT=stats.kruskal(ALT_I,ALTIII,ALT_V)
    
    #Bilt tot preqx
    #Biltotpreqx
    cur.execute('SELECT Biltotpreqx FROM Basecxcol WHERE Biltotpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    Biltotpreqx_I=cur.fetchall()
    
    avg_BiltotpreqxI=np.average(Biltotpreqx_I)
    
    u,shap_BiltotpreqxI=stats.shapiro(Biltotpreqx_I)
    
    #Biltotpreqx III
    cur.execute('SELECT Biltotpreqx FROM Basecxcol WHERE Biltotpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    BiltotpreqxIII=cur.fetchall()
    
    avg_BiltotpreqxIII_IV=np.average(BiltotpreqxIII)
    
    'shap_BiltotpreqxIII=stats.shapiro(BiltotpreqxIII)'
    
     #Biltotpreqx V
    cur.execute('SELECT Biltotpreqx FROM Basecxcol WHERE Biltotpreqx!=0 AND Comppostqx ="V" ')
    Biltotpreqx_V=cur.fetchall()
    
    avg_Biltotpreqx_V=np.average(Biltotpreqx_V)
    
    t,shap_Biltotpreqx_V=stats.shapiro(Biltotpreqx_V)
   
    i,kruskal_Biltotpreqx=stats.kruskal(Biltotpreqx_I,BiltotpreqxIII,Biltotpreqx_V)
    
    
    #INR
    #INRpreqx
    cur.execute('SELECT INRpreqx FROM Basecxcol WHERE INRpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    INRpreqx_I=cur.fetchall()
    
    avg_INRpreqxI=np.average(INRpreqx_I)
    
    u,shap_INRpreqxI=stats.shapiro(INRpreqx_I)
    
    #INRpreqx III
    cur.execute('SELECT INRpreqx FROM Basecxcol WHERE INRpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    INRpreqxIII=cur.fetchall()
    
    avg_INRpreqxIII_IV=np.average(INRpreqxIII)
    
    'shap_INRpreqxIII=stats.shapiro(INRpreqxIII)'
    
     #INRpreqx V
    cur.execute('SELECT INRpreqx FROM Basecxcol WHERE INRpreqx!=0 AND Comppostqx ="V" ')
    INRpreqx_V=cur.fetchall()
    
    avg_INRpreqx_V=np.average(INRpreqx_V)
    
    t,shap_INRpreqx_V=stats.shapiro(INRpreqx_V)
   
    i,kruskal_INRpreqx=stats.kruskal(INRpreqx_I,INRpreqxIII,INRpreqx_V)
    
    
    #Creatinina
    
     #Creatpreqx
    cur.execute('SELECT Creatpreqx FROM Basecxcol WHERE Creatpreqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    Creatpreqx_I=cur.fetchall()
    
    avg_CreatpreqxI=np.average(Creatpreqx_I)
    
    u,shap_CreatpreqxI=stats.shapiro(Creatpreqx_I)
    
    #Creatpreqx III
    cur.execute('SELECT Creatpreqx FROM Basecxcol WHERE Creatpreqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    CreatpreqxIII=cur.fetchall()
    
    avg_CreatpreqxIII_IV=np.average(CreatpreqxIII)
    
    'shap_CreatpreqxIII=stats.shapiro(CreatpreqxIII)'
    
     #Creatpreqx V
    cur.execute('SELECT Creatpreqx FROM Basecxcol WHERE Creatpreqx!=0 AND Comppostqx ="V" ')
    Creatpreqx_V=cur.fetchall()
    
    avg_Creatpreqx_V=np.average(Creatpreqx_V)
    
    t,shap_Creatpreqx_V=stats.shapiro(Creatpreqx_V)
   
    i,kruskal_Creatpreqx=stats.kruskal(Creatpreqx_I,CreatpreqxIII,Creatpreqx_V)
    
    
    #Tiempo de síntomas a tratamiento quirúrgico
    
     #Tiempo
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Tiempoinsintqx!=0 AND (Comppostqx ="I" OR Comppostqx="II")')
    Tiempoinsintqx_I=cur.fetchall()
    
    avg_TiempoinsintqxI=np.average(Tiempoinsintqx_I)
    
    u,shap_TiempoinsintqxI=stats.shapiro(Tiempoinsintqx_I)
    
    #Tiempoinsintqx III
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Tiempoinsintqx!=0 AND (Comppostqx ="III" OR Comppostqx="IV")')
    TiempoinsintqxIII=cur.fetchall()
    
    avg_TiempoinsintqxIII_IV=np.average(TiempoinsintqxIII)
    
    'shap_TiempoinsintqxIII=stats.shapiro(TiempoinsintqxIII)'
    
     #Tiempoinsintqx V
    cur.execute('SELECT Tiempoinsintqx FROM Basecxcol WHERE Tiempoinsintqx!=0 AND Comppostqx ="V" ')
    Tiempoinsintqx_V=cur.fetchall()
    
    avg_Tiempoinsintqx_V=np.average(Tiempoinsintqx_V)
    
    y,shap_Tiempoinsintqx_V=stats.shapiro(Tiempoinsintqx_V)
   
    r,kruskal_Tiempoinsintqx=stats.kruskal(Tiempoinsintqx_I,TiempoinsintqxIII,Tiempoinsintqx_V)
    
    
    #qSOFA
    
     #qSOFA
    cur.execute('SELECT qSOFApreqx FROM Basecxcol WHERE Comppostqx ="I" OR Comppostqx="II"')
    qSOFA_I=cur.fetchall()
    
    avg_qSOFAI=np.average(qSOFA_I)
    
    u,shap_qSOFAI=stats.shapiro(qSOFA_I)
    
    #qSOFA III
    cur.execute('SELECT qSOFApreqx FROM Basecxcol WHERE Comppostqx ="III" OR Comppostqx="IV"')
    qSOFAIII=cur.fetchall()
    
    avg_qSOFAIII_IV=np.average(qSOFAIII)
    
    'shap_qSOFAIII=stats.shapiro(qSOFAIII)'
    
     #qSOFA V
    cur.execute('SELECT qSOFApreqx FROM Basecxcol WHERE Comppostqx ="V" ')
    qSOFA_V=cur.fetchall()
    
    avg_qSOFA_V=np.average(qSOFA_V)
    
    y,shap_qSOFA_V=stats.shapiro(qSOFA_V)
   
    r,kruskal_qSOFA=stats.kruskal(qSOFA_I,qSOFAIII,qSOFA_V)
    
    data_1=[(Leu_I_II,avg_leuI_II,shap_LeuI,Leu_III_IV,avg_leuIII_IV,'-',Leu_V,avg_leuV,shap_V,kruskal_leu),
            (ADE_I_II,avg_ADEI_II,shap_ADEI,ADE_III_IV,avg_ADEIII_IV,shap_ADEIII_IV,ADE_V,avg_ADE_V,shap_ADE_V,kruskal_ade),
             (HTO_I,avg_HTOI,shap_HTOI,HTOIII,avg_HTOIII_IV,'shap_HTOIII',HTO_V,avg_HTO_V,shap_HTO_V,kruskal_HTO),
             (Plaq_I,avg_PlaqI,shap_PlaqI,PlaqIII,avg_PlaqIII_IV,'shap_PlaqIII',Plaq_V,avg_Plaq_V,shap_Plaq_V,kruskal_Plaq),
            (AST_I,avg_ASTI,shap_ASTI,ASTIII,avg_ASTIII_IV,'shap_ASTIII',AST_V,avg_AST_V,shap_AST_V,kruskal_AST),
            (ALT_I,avg_ALTI,shap_ALTI,ALTIII,avg_ALTIII_IV,'shap_ALTIII',ALT_V,avg_ALT_V,shap_ALT_V,kruskal_ALT),
            (Biltotpreqx_I,avg_BiltotpreqxI,shap_BiltotpreqxI,BiltotpreqxIII,avg_BiltotpreqxIII_IV,'shap_BiltotpreqxIII',Biltotpreqx_V,avg_Biltotpreqx_V,shap_Biltotpreqx_V,kruskal_Biltotpreqx),
            (INRpreqx_I,avg_INRpreqxI,shap_INRpreqxI,INRpreqxIII,avg_INRpreqxIII_IV,'shap_INRpreqxIII',INRpreqx_V,avg_INRpreqx_V,shap_INRpreqx_V,kruskal_INRpreqx),
            (Creatpreqx_I,avg_CreatpreqxI,shap_CreatpreqxI,CreatpreqxIII,avg_CreatpreqxIII_IV,'shap_CreatpreqxIII',Creatpreqx_V,avg_Creatpreqx_V,shap_Creatpreqx_V,kruskal_Creatpreqx),
            (Tiempoinsintqx_I,avg_TiempoinsintqxI,shap_TiempoinsintqxI,TiempoinsintqxIII,avg_TiempoinsintqxIII_IV,'shap_TiempoinsintqxIII',Tiempoinsintqx_V,avg_Tiempoinsintqx_V,shap_Tiempoinsintqx_V,kruskal_Tiempoinsintqx),
            (qSOFA_I,avg_qSOFAI,shap_qSOFAI,qSOFAIII,avg_qSOFAIII_IV,'shap_qSOFAIII',qSOFA_V,avg_qSOFA_V,shap_qSOFA_V,kruskal_qSOFA)]






    index=['Leucocitosis','ADE','HTO','Plaquetas cel/mm3','AST mg/dl','ALT mg/dl','Bilirrubina total mg/dl','INR',
           'Creatinina mg/dl','Tiempo de evolución (dias)','qSOFA']
    columnas='CD I y II','CD I y II (m)','Shapiro I y II','CD III y IV',' III y IV (m)','Shapiro III y IV' ,'CD V',' CD V (m)','Shapiro V',' Kruskall-Wallis'
    df_kruskal=pd.DataFrame(data_1,index,columnas)
    st.dataframe(df_kruskal)