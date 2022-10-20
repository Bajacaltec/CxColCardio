from ctypes.wintypes import PPOINT
from lib2to3.pgen2 import pgen
from modulefinder import packagePathMap
from statistics import mean, pvariance, variance
import statistics
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
    
    
    
    
    
    
    