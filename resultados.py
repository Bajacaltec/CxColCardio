from modulefinder import packagePathMap
from turtle import color, pensize, width
from pyparsing import col
import scipy
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

def a_excel():
    con=sqlite3.connect('Db.db')
    cur=con.cursor()
    
    selectall=cur.execute('SELECT * FROM Basecxcol')
    selectall_fetch=cur.fetchall()
    dfall=pd.DataFrame(selectall_fetch)
    dfell=dfall.describe()
    st.table(dfell)
    
    excel='df.xlsx'
    dfall.to_excel(excel)


def tabla1_bis():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    #Tabla imc características basales
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC <= 18.49')
    desnutricion=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC >= 18.49 AND IMC<=24.9')
    normal=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC >= 25 AND IMC<=29.9')
    sobrepeso=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC >=30 AND IMC<=34.9')
    Obesidad_I=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC >=35 AND IMC<=39.9')
    Obesidad_II=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE IMC >=40')
    Obesidad_III=cur.fetchone()
    
    
    tabla_imc=[desnutricion,normal,sobrepeso,Obesidad_I,Obesidad_II,Obesidad_III]
    index_imc=['Desnutrición','Normal','Sobrepeso','Obesidad I','Obesidad II','Obesidad III']
    col_imc=['Clasificación']
    
    tablaimcdf=pd.DataFrame(tabla_imc,index_imc,col_imc)
    st.table(tablaimcdf)
    
    tabla_IMC=cur.fetchall()
    st.table(tabla_IMC)
    
def tabla1():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    #Tabla 1 características basales
    
    cur.execute('SELECT AVG(Edad),avg(Peso),avg(Talla),avg(IMC) FROM Basecxcol ')
    
    tabla1_fetch,=cur.fetchall()
    

    st.info('Tabla1. Datos demográficos')
    
  
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo="Si"')
    tabsino,=cur.fetchone() 
    
    cur.execute('SELECT  AVG(Cajetillas) FROM Basecxcol WHERE Tabaquismo="Si"')
    It,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Diabetes%"')
    cron_diab,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Hipertensión%"')
    cron_hip,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Infarto%"')
    cron_iam,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Valvulopatia%" OR Crónicos LIKE "%Estenosis%"')
    cron_valv,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Fibrilación%"')
    cron_fib,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Insuficiencia%"')
    cron_ICC,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Miocardiopatia%"')
    cron_mioc,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Bloqueo%"')
    cron_bloq,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Dislipidemias%"')
    cron_dislip,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE "%Linfoma%" OR Crónicos LIKE "%Otros%"')
    cron_otros,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores= "Si"')
    vasop_preqx,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Diasventmec!= 0')
    ventpreqx,=cur.fetchone()
    
    index_tabla1=['Edad (𝛍)','Peso (𝛍)','Talla (𝛍)','IMC (𝛍)','Tabaquismo','IT (𝛍)','Diabetes mellitus','Hipertensión arterial','Infarto agudo al miocardio',
                  'Valvulopatia','Fibrilación auricular','Insuficiencia cardiáca','Miocardiopatia dilatada','Bloqueo auriculoventricular',
                  'Dislipidemias','Otros','Vasopresores prequirúrgicos','Ventilación mecánica']
    columnas_tabla1=['N']
    tabla1_data=[tabla1_fetch[0],tabla1_fetch[1],tabla1_fetch[2],tabla1_fetch[3],tabsino,It,cron_diab,cron_hip,cron_iam,
                 cron_valv,cron_fib,cron_ICC,cron_mioc,cron_bloq,cron_dislip,cron_otros,
                 vasop_preqx,ventpreqx]
    df_tabla1=pd.DataFrame(tabla1_data,index_tabla1,columnas_tabla1)
    
    st.table(df_tabla1)
    
    df_tabla1.to_excel('/Users/alonso/CxColCardio/Tabla1.xlsx')
    con.close()
    
def tabla2():
    #Clínica
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    
    # Agregar ASA
    #
    #Causas de PA
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%Infarto%"')
    PA_infarto,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%Marcapaso%"')
    PA_marcapaso,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%Cateterismo%"')
    PA_cat,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%Valvular%"')
    PA_valv,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%Cirugia%"')
    PA_cx,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE "%ICC%"')
    PA_icc,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Edad>1 ')
    count_n,=cur.fetchone()
    
    
    PA_ccla=count_n-(PA_infarto+PA_marcapaso+PA_cat+PA_valv+PA_cx+PA_icc)
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%hipocondrio%"')
    sint_hipoder,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Nausea%"')
    sint_nausea,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Murphy%"')
    sint_Murphy,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Ictericia%"')
    sint_icter,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Fiebre%"')
    sint_fieb,=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Difuso%"')
    sint_abddif,=cur.fetchone()
    
    #Hallazgos por ultrasonido
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%perivesicular%"')
    usg_liqperi=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Engrosamiento%"')
    usg_engros=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Distensión%"')
    usg_diste=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Litiasis%"')
    usg_lit=cur.fetchone()
    
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
    
    #ASA
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="I"')
    asa_I=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="II"')
    asa_II=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="III"')
    asa_III=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="IV"')
    asa_IV=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="V"')
    asa_V=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE asa="VI"')
    asa_VI=cur.fetchone()
    
    #TOKYO
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tokyo="Leve"')
    tok_leve=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tokyo="Moderado"')
    tok_mod=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tokyo="Severo"')
    tok_sev=cur.fetchone()
    
    
    
    
    
    
    
    #Tabla
    st.info('Tabla 2. Clínica')
    index_tabla2=['N']
    tabla2=pd.DataFrame({'Infarto agudo al miocardio':PA_infarto,'Colocación de marcapaso':PA_marcapaso,'Cateterismo cardiáco':PA_cat,'Reemplazo valvular':PA_valv,'Cirugía cardiovascular':PA_cx,'Insuficiencia cardiáca':PA_icc,'Colecistitis aguda':PA_ccla,'Dolor en hipocondrio derecho':sint_hipoder,'Nausea':sint_nausea,'Signo de Murphy':sint_Murphy,'Ictericia':sint_icter,'Fiebre':sint_fieb,'Dolor abdominal difuso':sint_abddif,
                         'Líquido perivesicular':usg_liqperi,'Engrosamiento de pared vesicular':usg_engros,'Hidrocolecisto':usg_diste,'Litiasis vesicular':usg_lit,'Lodo vesicular':usg_Lodo,'Dilatación de la vía biliar':usg_dil,'Hallazgos TAC':1,
                         'Estriación de la grasa perivesicular':tac_estriacion,'Hidrocolecisto':tac_hidro,'Líquido perivesicular':tac_líquido,'Engrosamiento de la pared':tac_engrosamiento,
                         'Litiasis vesicular':tac_litiasis,'Reforzamiento de pared vesicular':tac_reforz,'Litiasis en vía biliar':tac_litobil,
                         'ASA I':asa_I,'ASA II':asa_II,'ASA III':asa_III,'ASA IV':asa_IV,'ASA V':asa_V,'ASA VI':asa_VI,
                         'Tokyo I':tok_leve,'Tokyo II':tok_mod,'Tokyo III':tok_sev},index=index_tabla2)
    #Para cambiar la orientación del DF se pone. T
    tabla2f=tabla2.T
    tabla2f.to_excel('/Users/alonso/CxColCardio/Tabla2.xlsx')

    st.table(tabla2.T)
    
def tabla3():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    
    
    #qSOFA ingreso
    
    
    #sSOFA
    st.info('Tabla no. 3. Cirugía')
    
    cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx!=0  ')
    iniciosint_avg=cur.fetchone()
    
    cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE Duracionqx!=0 AND Duracionqx!=1  ')
    duracion_cx=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE tipoqx="Laparoscopica"')
    laparos=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE tipoqx="Abierta"')
    abierta=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Conversión=1')
    conversion=cur.fetchone()
    
    #tipo de ccla
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tipoccla="Alitiasica"')
    alitiasica=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Tipoccla="Litiasica"')
    litiasica=cur.fetchone()
    
    #Hallazgos quirúrgicos
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Distensión%"')
    hall_distensión=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%necrosis vesicular%"')
    hall_necrosisves=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Necrosis de cístico%"')
    hall_necrosiscist=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Líquido perivesicular%"')
    hall_liqperives=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Engrosamiento%"')
    hall_engros=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Litiasis%"')
    hall_lit=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Piocolecisto%"')
    hall_pio=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%perforación vesicular%"')
    hall_perf=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Hallazgoscx LIKE "%Trombosis%"')
    hall_trombosis=cur.fetchone()
    
    
    #Postquirúrgico
    
    cur.execute('SELECT AVG(Diasestancia) FROM Basecxcol WHERE Diasestancia!=0  ')
    estancia_posqx=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE postqxvasopresor="Si"')
    vasop_posqx=cur.fetchone()
    
    #Clavien-dindo
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Comppostqx="I"')
    clavien_I=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Comppostqx="II"')
    clavien_II=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Comppostqx="III"')
    clavien_III=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Comppostqx="IV"')
    clavien_IV=cur.fetchone()
    
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Comppostqx="V"')
    clavien_V=cur.fetchone()
    
    #Mortalidad
    cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Muerte="Si"')
    mort=cur.fetchone()
    
    tabla3=pd.DataFrame({'Tiempo de inicio de síntomas hasta el tratamiento quirúrgico':iniciosint_avg,'Tiempo quirúrgico':duracion_cx
,                         'Cirugía laparoscópica':laparos,'Cirugía abierta':abierta,'Cirugía convertida':conversion,'Colecistitis litiasica':litiasica,'Colecistitis alitiásica':alitiasica,
'Hidrocolecisto':hall_distensión,'Necrosis vesicular':hall_necrosisves,'Necrosis del conducto cístico':hall_necrosiscist,'Líquido perivesicular':hall_liqperives,'Engrosamiento de pared vesicular':hall_engros,'Litiasis vesicular':hall_lit,'Piocolecisto':hall_pio,'Perforación vesicular':hall_perf,'Trombosis de artería cística':hall_trombosis,'Estancia postquirúrgica':estancia_posqx,'Vasopresor postquirúrgico':vasop_posqx,
'Clavien-Dindo I':clavien_I,'Clavien-Dindo II':clavien_II,'Clavien-Dindo III':clavien_III,'Clavien-Dindo IV':clavien_IV,'Clavien-Dindo V':clavien_V,
'Mortalidad':mort},index=['N'])
    
    tabla3t=tabla3.T
    tabla3t.to_excel('/Users/alonso/CxColCardio/Tabla3.xlsx')
    st.table(tabla3t)
    
def tabla4():
    st.info('Tabla No. 4 Predictores de morbimortalidad')
    
    #Tabla para predictores de morbimortalidad como laboratorios de ingrso vs preqx, etc.
    con=sqlite3.connect('Db.DB')
    cur=con.cursor()
    
    #FC
    cur.execute('SELECT AVG(FCing) FROM Basecxcol WHERE Muerte!="Si" AND (Comppostqx="V" OR Comppostqx!="IV" OR Comppostqx!="III")')
    fcing_av,=cur.fetchone()
    
    cur.execute('SELECT AVG(FCpreqx) FROM Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"') 
    fc_preqx_avg,=cur.fetchone()
    
    #FC alta morbimorta
    cur.execute('SELECT AVG(FCing) FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    fc_ing_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Fcpreqx) FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    fc_preqx_mort,=cur.fetchone()
    
    #FR
    cur.execute('SELECT AVG(FRing) FROM Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"' )
    fr_ing,=cur.fetchone()
    
    cur.execute('SELECT AVG(FRpreqx) FROM Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    fr_preqx,   =cur.fetchone()
    
    #FR CD>III
    cur.execute('SELECT AVG(FRing) FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"'  )
    fr_ing_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(FRpreqx) FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    fr_preqx_mort, =cur.fetchone()
    
    #Sistólica
    cur.execute('SELECT AVG(Sising) FROM Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    sis_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Sistpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    sis_preqx_avg,=cur.fetchone()
    
    #Sistólica CD>III
    cur.execute('SELECT AVG(Sising) FROM Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    sis_ing_avg_MORT,=cur.fetchone()
    
    cur.execute('SELECT AVG(Sistpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    sis_preqx_avg_mort,=cur.fetchone()
    
    #Diastólica
    cur.execute('SELECT AVG(Diasing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    diast_in_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Diastpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    diast_preqx_avg,=cur.fetchone()
    
    #Diastólica CD>III
    cur.execute('SELECT AVG(Diasing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III" ')
    diast_in_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Diastpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    diast_preqx_avg_mort,=cur.fetchone()
    
    #Temp
    cur.execute('SELECT AVG(Temping) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    temp_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Temppreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    temp_preqx,=cur.fetchone()
    
    #TEmp CD>III
    cur.execute('SELECT AVG(Temping) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    temp_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Temppreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    temp_preqx_mort,=cur.fetchone()
    
    #Leu
    cur.execute('SELECT AVG(Leuing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    leu_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Leupreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    leu_preqx,=cur.fetchone()
     #Leu CD>III
    cur.execute('SELECT AVG(Leuing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    leu_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Leupreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    leu_preqx_mort,=cur.fetchone()
    
    #HTO
    cur.execute('SELECT AVG(Hematocritoing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    hto_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(HTOpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    hto_preqx,=cur.fetchone()
     #HTO CD>III
    cur.execute('SELECT AVG(Hematocritoing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    hto_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(HTOpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    hto_preqx_mort,=cur.fetchone()
    
    #ADE
    cur.execute('SELECT AVG(ADEing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    ade_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(ADEpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    ade_preqx,=cur.fetchone()
    
     #ADE CD>III
    cur.execute('SELECT AVG(ADEing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ade_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(ADEpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ade_preqx_mort,=cur.fetchone()
    
    
    #plaq
    cur.execute('SELECT AVG(Plaquetasing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    plaq_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Plaqpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    plaq_preqx,=cur.fetchone()
    
     #plaq CD>III
    cur.execute('SELECT AVG(Plaquetasing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    plaq_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Plaqpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    plaq_preqx_mort,=cur.fetchone()
    
    #AST
    cur.execute('SELECT AVG(ASTing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    ast_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(ASTpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    ast_preqx,=cur.fetchone()
    
     #AST CD>III
    cur.execute('SELECT AVG(ASTing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ast_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(ASTpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ast_preqx_mort,=cur.fetchone()
    
    #ALT
    cur.execute('SELECT AVG(ALTing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    alt_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(ALTpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    alt_preqx,=cur.fetchone()
    
     #ALT CD>III
    cur.execute('SELECT AVG(ALTing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    alt_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(ALTpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    alt_preqx_mort,=cur.fetchone()
    
     #Bil
    cur.execute('SELECT AVG(Biltoting) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    bil_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Biltotpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    bil_preqx,=cur.fetchone()
    
     #Bil CD>III
    cur.execute('SELECT AVG(Biltoting) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    bil_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Biltotpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    bil_preqx_mort,=cur.fetchone()
    
     #FA
    cur.execute('SELECT AVG(FAing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    FA_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(FApreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    FA_preqx,=cur.fetchone()
    
     #FA CD>III
    cur.execute('SELECT AVG(FAing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    FA_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(FApreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    FA_preqx_mort,=cur.fetchone()
    
         #INR
    cur.execute('SELECT AVG(INRing) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    INR_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(INRpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    INR_preqx,=cur.fetchone()
    
     #INR CD>III
    cur.execute('SELECT AVG(INRing) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    INR_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(INRpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    INR_preqx_mort,=cur.fetchone()
    
        #Creatinina
    cur.execute('SELECT AVG(Creating) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    Creat_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(Creatpreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    Creat_preqx,=cur.fetchone()
    
     #Creatinina CD>III
    cur.execute('SELECT AVG(Creating) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    Creat_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(Creatpreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    Creat_preqx_mort,=cur.fetchone()
    
      #qSOFA
    cur.execute('SELECT AVG(qSOFA) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    qsofa_ing_avg,=cur.fetchone()
    
    cur.execute('SELECT AVG(qSOFApreqx) From Basecxcol WHERE Muerte!="Si" OR Comppostqx!="V" OR Comppostqx!="IV" OR Comppostqx!="III"')
    qsofa_preqx,=cur.fetchone()
    
     #qSOFA CD>III
    cur.execute('SELECT AVG(qSOFA) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    qsofa_ing_avg_mort,=cur.fetchone()
    
    cur.execute('SELECT AVG(qSOFApreqx) From Basecxcol WHERE Muerte="Si" OR Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    qsofa_preqx_mort,=cur.fetchone()
    
    
    data_comp=[(fcing_av,fc_preqx_avg),(fc_ing_mort,fc_preqx_mort),(fr_ing,fr_preqx),(fr_ing_mort,fr_preqx_mort),(sis_ing_avg,sis_preqx_avg),(sis_ing_avg_MORT,sis_preqx_avg_mort),(diast_in_avg,diast_preqx_avg),(diast_in_avg_mort,diast_preqx_avg_mort),
               (temp_ing_avg,temp_preqx),(temp_ing_avg_mort,temp_preqx_mort),(leu_ing_avg,leu_preqx),(leu_ing_avg_mort,leu_preqx_mort),
               (hto_ing_avg,hto_preqx),(hto_ing_avg_mort,hto_preqx_mort),(ade_ing_avg,ade_preqx),(ade_ing_avg_mort,ade_preqx_mort),
               (plaq_ing_avg,plaq_preqx),(plaq_ing_avg_mort,plaq_preqx_mort),(ast_ing_avg,ast_preqx),(ast_ing_avg_mort,ast_preqx_mort),
               (alt_ing_avg,alt_preqx),(alt_ing_avg_mort,alt_preqx_mort),(bil_ing_avg,bil_preqx),(bil_ing_avg_mort,bil_preqx_mort),(FA_ing_avg,FA_preqx),(FA_ing_avg_mort,FA_preqx_mort),
               (INR_ing_avg,INR_preqx),(INR_ing_avg_mort,INR_preqx_mort),(Creat_ing_avg,Creat_preqx),(Creat_ing_avg_mort,Creat_preqx_mort),(qsofa_ing_avg,qsofa_preqx),(qsofa_ing_avg_mort,qsofa_preqx_mort)]
    data_comp_index=['Frecuencia cardiáca/min *','Frecuencia cardiáca CD >III','Frecuencia respiratoria/min CD<III','Frecuencia respiratoria/min CD >III','Presión sistólica mmHg CD<III','Presión sistólica mmHg CD>III','Presión diastólica mmHg CD<III ','Presión diastólica mmHg CD>III ',
                     'Temperatura °C CD <III','Temperatura °C CD >III','Leucocitos mm3 CD <III','Leucocitos mm3 CD>III','Hematocrito','Hematocrito CD>III',
                     'ADE','ADE CD>III','Plaquetas mm3','Plaquetas mm3 CD>III','AST mg/dl','AST mg/dl CD>III','ALT mg/dl','ALT mg/dl CD>III',
                     'Bilirrubina total mg/dl','Bilirrubina total mg/dl CD>III','Fosfatasa alcalina (mg/dl)','Fosfatasa alcalina (mg/dl) CD>III','INR','INR CD>III','Creatinina (mg/dl)','Creatinina (mg/dl) CD>III',
                     'qSOFA','qSOFA CD>III']
    data_comp_columns=['Ingreso','Prequirúrgica']
    df_comparacion=pd.DataFrame(data_comp,index=data_comp_index,columns=data_comp_columns)
    dfcomp_arevs=df_comparacion.T
    st.table(df_comparacion )
    
    tabla4excel=df_comparacion.to_excel('Tabla4.xlsx')
    #Seleccionar los  labs de ingreso y prequirúrgicos de los pacients con morbi-morta elevados en una fila
    #Seleciconar los labs de ingreso y prequirúrgicos de los pacientes con morbi-morta bajos en otra fila
    
    # en el articulo de laurila comparan el SOFA en admisión entre dos grupos (muertos vs vivos) y luego prequirúrgico
    #entre muertos y vivos
    

def tabla5():
    st.info('Tabla no. 5. Factores asociados a aumento en la morbimortalidad')
    con=sqlite3.connect('Db.db')
    cur=con.cursor()
    
    #Edad 
    pruebaf=cur.execute('SELECT AVG(Edad) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    edad_vivo,=cur.fetchone()
    #Edad CD>III
    cur.execute('SELECT AVG(Edad) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    edad_morta,=cur.fetchone()
    
    #Género, como comparar genero????
    
    #Peso
    cur.execute('SELECT AVG(Peso) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    peso_vivo,=cur.fetchone()
    
    #Peso mort
    cur.execute('SELECT AVG(Peso) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    peso_mort,=cur.fetchone()
    
     #IMC
    cur.execute('SELECT AVG(IMC) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    IMC_vivo,=cur.fetchone()
    
    #IMC mort
    cur.execute('SELECT AVG(IMC) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    IMC_mort,=cur.fetchone()
    
    #Ventmeca preqx
    cur.execute('SELECT AVG(Diasventmec) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    Ventmecpreqx,=cur.fetchone()
    
    #Ventmec preqx mort
    cur.execute('SELECT AVG(Diasventmec) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ventmecpreqx_mort,=cur.fetchone()
    
    # ADE ing
    cur.execute('SELECT AVG(ADEing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    ade_ing,=cur.fetchone()
    
    # ADE ingmort
    cur.execute('SELECT AVG(ADEing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ADEING_mort,=cur.fetchone()
    
    # ADE preqx
    cur.execute('SELECT AVG(ADEpreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    ade_preqx,=cur.fetchone()
    
    # ADE preqxmort
    cur.execute('SELECT AVG(ADEpreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ADEpreqx_mort,=cur.fetchone()
    
    # leu ing
    cur.execute('SELECT AVG(Leuing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    leu_ing,=cur.fetchone()
    
    # leu ing_mort
    cur.execute('SELECT AVG(Leuing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    leu_ing_mort,=cur.fetchone()
    
    # leu preqx
    cur.execute('SELECT AVG(Leupreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    leu_preqx,=cur.fetchone()
    
    # leu preqx_mort
    cur.execute('SELECT AVG(Leupreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    leu_preqx_mort,=cur.fetchone()
    
    # HB ing
    cur.execute('SELECT AVG(Hematocritoing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    hb_ing,=cur.fetchone()
    
    # HB ing_mort
    cur.execute('SELECT AVG(Hematocritoing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    hb_ing_mort,=cur.fetchone()
    
     # HB preqx
    cur.execute('SELECT AVG(HTOpreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    hb_preqx,=cur.fetchone()
    
    # HB preqx_mort
    cur.execute('SELECT AVG(HTOpreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    hb_preq_mort,=cur.fetchone()
    
      # plaq ing
    cur.execute('SELECT AVG(Plaquetasing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    plaq_ing,=cur.fetchone()
    
    # plaq ing_mort
    cur.execute('SELECT AVG(Plaquetasing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    plaq_ing_mort,=cur.fetchone()
    
     # plaq_preqx ing
    cur.execute('SELECT AVG(Plaqpreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    plaq_preqx,=cur.fetchone()
    
    # plaq preqx_mort
    cur.execute('SELECT AVG(Plaqpreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    plaq_preqx_mort,=cur.fetchone()
    
     # AST ing
    cur.execute('SELECT AVG(ASTing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    AST_ing,=cur.fetchone()
    
    # AST ing_mort
    cur.execute('SELECT AVG(ASTing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    AST_ing_mort,=cur.fetchone()
    
    # AST preqx
    cur.execute('SELECT AVG(ASTpreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    AST_preqx,=cur.fetchone()
    
    # AST preqx_mort
    cur.execute('SELECT AVG(ASTpreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    AST_preqx_mort,=cur.fetchone()
    
    # ALT ingreso
    cur.execute('SELECT AVG(ALTing) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    ALT_ing,=cur.fetchone()
    
    # ALT ing_mort
    cur.execute('SELECT AVG(ALTing) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ALT_ing_mort,=cur.fetchone()
    
    # ALT preqx
    cur.execute('SELECT AVG(ALTpreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    ALT_preqx,=cur.fetchone()
    
    # ALT preqx_mort
    cur.execute('SELECT AVG(ALTpreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    ALT_preqx_mort,=cur.fetchone()
    
     # Bil tot ing
    cur.execute('SELECT AVG(Biltoting) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    biltot_ing,=cur.fetchone()
    
    # Bil tot_mort
    cur.execute('SELECT AVG(Biltoting) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    biltoting_mort,=cur.fetchone()
    
      # Bil tot preqx
    cur.execute('SELECT AVG(Biltotpreqx) FROM Basecxcol WHERE Biltoting!=1 AND Comppostqx="I" OR Comppostqx="II"')
    biltot_preqx,=cur.fetchone()
    
    # Bil tot_mort preqx
    cur.execute('SELECT AVG(Biltotpreqx) FROM Basecxcol WHERE Biltoting!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    biltot_preqx_mort,=cur.fetchone()
    
      # INR ing
    cur.execute('SELECT AVG(INRing) FROM Basecxcol WHERE INRing!=1 AND Comppostqx="I" OR Comppostqx="II"')
    INR_ing,=cur.fetchone()
    
    #INR ing mort
    cur.execute('SELECT AVG(INRing) FROM Basecxcol WHERE INRing!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    INR_ing_mort,=cur.fetchone()
    
        # INR preqx
    cur.execute('SELECT AVG(INRpreqx) FROM Basecxcol WHERE INRpreqx!=1 AND Comppostqx="I" OR Comppostqx="II"')
    INR_preqx,=cur.fetchone()
    
    #INR preqx mort
    cur.execute('SELECT AVG(INRpreqx) FROM Basecxcol WHERE INRpreqx!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    INR_preqx_mort,=cur.fetchone()

       # Creat ing
    cur.execute('SELECT AVG(Creating) FROM Basecxcol WHERE Creating!=1 AND Comppostqx="I" OR Comppostqx="II"')
    creating,=cur.fetchone()
    
    #Creat ing mort
    cur.execute('SELECT AVG(Creating) FROM Basecxcol WHERE Creating!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    creating_mort,=cur.fetchone()
    
    
       # Creat preqrx
    cur.execute('SELECT AVG(Creatpreqx) FROM Basecxcol WHERE Creatpreqx!=1 AND Comppostqx="I" OR Comppostqx="II"')
    creatpreqx,=cur.fetchone()
    
    #Creat preqx mort
    cur.execute('SELECT AVG(Creatpreqx) FROM Basecxcol WHERE Creatpreqx!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    creatpreqx_mort,=cur.fetchone()
    
      # tiempo 
    cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx!=1 AND Comppostqx="I" OR Comppostqx="II"')
    tiemposintqx,=cur.fetchone()
    
    #tiempo qx  mort
    cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE Tiempoinsintqx!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    tiemposint_mort,=cur.fetchone()
    
        # duración qx 
    cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE Duracionqx!=1 AND Comppostqx="I" OR Comppostqx="II"')
    duracioncx,=cur.fetchone()
    
    #duración qx  mort
    cur.execute('SELECT Duracionqx FROM Basecxcol WHERE Duracionqx!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    datos_duracion=cur.fetchall()

    cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE Duracionqx!=1 AND Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    duracioncx_mort,=cur.fetchone()
    
       # estancia pos qx 
    cur.execute('SELECT AVG(Diasestancia) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    diasestancia,=cur.fetchone()
    
    #estancia qx  mort
    cur.execute('SELECT AVG(Diasestancia) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    estancia_mort,=cur.fetchone()
    
     # estancia qSOFA ing 
    cur.execute('SELECT AVG(qSOFA) FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II")')
    qsofa,=cur.fetchone()
    
    #estancia qSOFA ing  mort
    cur.execute('SELECT AVG(qSOFA) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    qsofa_mort,=cur.fetchone()
    
         # estancia qSOFA preqx 
    cur.execute('SELECT AVG(qSOFApreqx) FROM Basecxcol WHERE Comppostqx="I" OR Comppostqx="II"')
    qsofa_preqx,=cur.fetchone()
    
    #estancia qSOFA preqx  mort
    cur.execute('SELECT AVG(qSOFApreqx) FROM Basecxcol WHERE Comppostqx="V" OR Comppostqx="IV" OR Comppostqx="III"')
    qsofa_preqx_mort,=cur.fetchone()
    
    cur.execute('SELECT Cajetillas FROM Basecxcol WHERE Cajetillas!="NA"')
    duracioncx_1=cur.fetchall()
    st.table(duracioncx_1)
    tiempocxccx=pd.DataFrame(duracioncx_1)
    tiempodesc=tiempocxccx.describe()
    st.dataframe(tiempodesc)
    datos_mortalidad=[(edad_vivo,edad_morta),(peso_vivo,peso_mort),(IMC_vivo,IMC_mort),(Ventmecpreqx,ventmecpreqx_mort),(ade_ing,ADEING_mort),
                      (ade_preqx,ADEpreqx_mort),(leu_ing,leu_ing_mort),(leu_preqx,leu_preqx_mort),(hb_ing,hb_ing_mort),(hb_preqx,hb_preq_mort),
                      (plaq_ing,plaq_ing_mort),(plaq_preqx,plaq_preqx_mort),(AST_ing,AST_ing_mort),(AST_preqx,AST_preqx_mort),(ALT_ing,ALT_ing_mort),
                      (ALT_preqx,ALT_preqx_mort),(biltot_ing,biltoting_mort),(biltot_preqx,biltot_preqx_mort),(INR_ing,INR_ing_mort),(INR_preqx,INR_preqx_mort),
                      (creating,creating_mort),(creatpreqx,creatpreqx_mort),(tiemposintqx,tiemposint_mort),(duracioncx,duracioncx_mort),(diasestancia,estancia_mort),
                      (qsofa,qsofa_mort),(qsofa_preqx,qsofa_preqx_mort)]
    index_data_mort=['Edad (Años)','Peso (Kg)','IMC','Ventilación mecánica prequirúrgica','ADE ingreso','ADE prequirúrgico','Leucocitosis ingreso (cel/mm3)','Leucocitosis prequirúrgica (cel/mm3)',
                     'Hemoglobina de ingreso (mg/dl)','Hemoglobina prequirúrgica (mg/dl)','Plaquetas ingreso','Plaquetas prequirúrgicas','AST ingreso (mg/dl)',
                     'AST prequirúrgica (mg/dl)','ALT ingreso (mg/dl)','ALT prequirúrgico (mg/dl)','Bilirrubina total * (mg/dl)','Bilirrubina total prequirúrgica (mg/dl)',
                     'INR ingreso','INR prequirúrgica','Creatinina * (mg/dl)','Creatinina prequirúrgica (mg/dl)','Tiempo de inicio de síntomas (días)','Duración de cirugía (min)','Dias de estancia (días)',
                     'qSOFA ingreso','qSOFA prequirúrgico ']
    columna_mort_data=['CD<II','CD>III']
    
    df_data_mort=pd.DataFrame(datos_mortalidad,index_data_mort,columna_mort_data)
    st.table(df_data_mort)
    
def tabla6():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    #ASAI
    asaI=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="I" AND Comppostqx="I" ) OR (asa="I" AND Comppostqx= "II" )')
    asaI_res,=cur.fetchone()
    
    
    asaI_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="I" AND Comppostqx="III") OR (asa="I" AND Comppostqx="IV") ')
    asaI_res_morb,=cur.fetchone()
    
    #ASA I MORTalidad
    asaI_mort_no=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="I" AND Comppostqx!="V"')
    asaI_res_mort_no,=cur.fetchone()
    
    
    asaI_mortalidad=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="I" AND Comppostqx="V" ')
    asaI_res_mortalidad,=cur.fetchone()
    
    #ASA II
    
    asaII=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="I" ) OR (asa="II" AND Comppostqx= "II" ) ')
    asaII_res,=cur.fetchone()
    
    asaII_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="II" AND Comppostqx="III") OR (asa="II" AND Comppostqx="IV")  ')
    asaII_res_morb,=cur.fetchone()
    
     #ASA IImortalidad
    
    asaII_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="II" AND Comppostqx!="V" ')
    asaII_res_mortno,=cur.fetchone()
    
    asaII_mortalidad=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="II" AND Comppostqx="V" ')
    asaII_res_mortalidad,=cur.fetchone()
    
        #ASA III
    
    asaIII=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="I" ) OR (asa="III" AND Comppostqx= "II" ) ')
    asaIII_res,=cur.fetchone()
    
    asaIII_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="III" AND Comppostqx="III") OR (asa="III" AND Comppostqx="IV") ')
    asaIII_res_morb,=cur.fetchone()
    
     #ASA III Mortalidad
    
    asaIII_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="III" AND Comppostqx!="V"  ')
    asaIII_res_mortno,=cur.fetchone()
    
    asaIII_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="III" AND Comppostqx="V" ')
    asaIII_res_mort,=cur.fetchone()
    
     #ASA IV
    
    asaIV=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="I" ) OR (asa="IV" AND Comppostqx= "II" ) ')
    asaIV_res,=cur.fetchone()
    
    asaIV_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="IV" AND Comppostqx="III") OR (asa="IV" AND Comppostqx="IV")')
    asaIV_res_morb,=cur.fetchone()
    
     #ASA IV mortalidad
    
    asaIV_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="IV" AND Comppostqx!="V" ')
    asaIV_res_mortno,=cur.fetchone()
    
    asaIV_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="IV" AND Comppostqx="V"')
    asaIV_res_mort,=cur.fetchone()
    
     #ASA V
    
    asaV=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="V" AND Comppostqx="I" ) OR (asa="V" AND Comppostqx= "II" ) ')
    asaV_res,=cur.fetchone()
    
    asaV_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="V" AND Comppostqx="III") OR (asa="V" AND Comppostqx="IV") ')
    asaV_res_morb,=cur.fetchone()
    
     #ASA V mortalidad
    
    asaV_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="V" AND Comppostqx!="V"  ')
    asaV_res_mortno,=cur.fetchone()
    
    asaV_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="V" AND Comppostqx="V"  ')
    asaV_res_mort,=cur.fetchone()
    
    #ASA VI
    
    asaVI=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="VI" AND Comppostqx="I" ) OR (asa="VI" AND Comppostqx= "II" ) ')
    asaVI_res,=cur.fetchone()
    
    asaVI_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (asa="VI" AND Comppostqx="III") OR (asa="VI" AND Comppostqx="IV")  ')
    asaVI_res_morb,=cur.fetchone()
    
    #ASA VI mortalidad
    
    asaVI_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="VI" AND Comppostqx!="V" ')
    asaVI_res_mortno,=cur.fetchone()
    
    asaVI_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE asa="VI" AND Comppostqx="V" ')
    asaVI_res_mort,=cur.fetchone()
    
     #Tokyo I
    
    Tokyo_I=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Leve" AND Comppostqx="I" ) OR (Tokyo="Leve" AND Comppostqx= "II" ) ')
    Tokyo_I_res,=cur.fetchone()
    
    Tokyo_I_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Leve" AND Comppostqx="III") OR (Tokyo="Leve" AND Comppostqx="IV") ')
    Tokyo_I_res_morb,=cur.fetchone()
    
    #Tokyo I_mortliadad
    
    Tokyo_I_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Leve" AND Comppostqx!="V" ')
    Tokyo_I_res_mortno,=cur.fetchone()
    
    Tokyo_I_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Leve" AND Comppostqx="V"')
    Tokyo_I_res_mort,=cur.fetchone()
    
    
    #Tokyo II
    
    Tokyo_II=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Moderado" AND Comppostqx="I" ) OR (Tokyo="Moderado" AND Comppostqx= "II" ) ')
    Tokyo_II_res,=cur.fetchone()
    
    Tokyo_II_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Moderado" AND Comppostqx="III") OR (Tokyo="Moderado" AND Comppostqx="IV")  ')
    Tokyo_II_res_morb,=cur.fetchone()
    
    #Tokyo II_mortalidad
    
    Tokyo_II_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Moderado" AND Comppostqx!="V" ')
    Tokyo_II_res_mortno,=cur.fetchone()
    
    Tokyo_II_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Moderado" AND Comppostqx="V"  ')
    Tokyo_II_res_mort,=cur.fetchone()
    
    #Tokyo III
    
    Tokyo_III=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Severo" AND Comppostqx="I" ) OR (Tokyo="Severo" AND Comppostqx= "II" ) ')
    Tokyo_III_res,=cur.fetchone()
    
    Tokyo_III_morb=cur.execute('SELECT Count(*) FROM Basecxcol WHERE (Tokyo="Severo" AND Comppostqx="III") OR (Tokyo="Severo" AND Comppostqx="IV")  ')
    Tokyo_III_res_morb,=cur.fetchone()
    
    #Tokyo III_mortalidad
    
    Tokyo_III_mortno=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Severo" AND Comppostqx!="V" ')
    Tokyo_III_res_mortno,=cur.fetchone()
    
    Tokyo_III_mort=cur.execute('SELECT Count(*) FROM Basecxcol WHERE Tokyo="Severo" AND Comppostqx="V" ')
    Tokyo_III_res_mort,=cur.fetchone()
    
   
    
    datacualitativ_morbmort=[(asaI_res,asaI_res_morb,asaI_res_mort_no,asaI_res_mortalidad),(asaII_res,asaII_res_morb,asaII_res_mortno,asaII_res_mortalidad),(asaIII_res,asaIII_res_morb,asaIII_res_mortno,asaIII_res_mort),(asaIV_res,asaIV_res_morb,asaIV_res_mortno,asaIV_res_mort),(asaV_res,asaV_res_morb,asaV_res_mortno,asaV_res_mort),(asaVI_res,asaVI_res_morb,asaVI_res_mortno,asaVI_res_mort),
                             (Tokyo_I_res,Tokyo_I_res_morb,Tokyo_I_res_mortno,Tokyo_I_res_mort),(Tokyo_II_res,Tokyo_II_res_morb,Tokyo_II_res_mortno,Tokyo_II_res_mort),(Tokyo_III_res,Tokyo_III_res_morb,Tokyo_III_res_mortno,Tokyo_III_res_mort)]
    index_datacualitativ_mort=['ASA I','ASA II','ASA III','ASA IV','ASA V','ASA VI','Tokyo I','Tokyo II','Tokyo III']
    col_datacualitativ_mort=['CD<III','CD III y IV','Supervivientes','Mortalidad']
    dtacual_mort=pd.DataFrame(datacualitativ_morbmort,index_datacualitativ_mort,col_datacualitativ_mort)
    st.table(dtacual_mort)
    
    
def tablano7():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    
    #Leucocitosis prequirúrgica
    #morbilidad baja
    leu_morb_baja=cur.execute('SELECT AVG(Leupreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Leupreqx!=0)')
    leumorbaja_res,=cur.fetchone()    
    
    #Morb alta
    leu_morb_alta=cur.execute('SELECT AVG(Leupreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Leupreqx!=0)')
    leumoralta_res,=cur.fetchone()
    
    
    cun=sqlite3.connect('DB.db')
    cun.row_factory = lambda cursor, row: row[0]
    # con el rowfactory se toma solo la primera parte de la columna y te la pone en forma de lista y no tupple
    c=cun.cursor()
    #p de leucocitosis y morbilidad
    p_leumorb=c.execute('SELECT Leupreqx FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Leupreqx!=0)')
    pleumorb_baja=c.fetchall()
    
    shap_pleumorbaja=stats.shapiro(pleumorb_baja)
    
    st.write(shap_pleumorbaja)
    
    p_leu_morb_alta=c.execute('SELECT Leupreqx FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Leupreqx!=0)')
    p_leumoralta_res=c.fetchall()
    st.info(p_leumoralta_res)
    pd_p_leumoralta=pd.Series(p_leumoralta_res)
    
    pmorbfinal=stats.mannwhitneyu(pleumorb_baja,p_leumoralta_res)
    st.warning(pmorbfinal)
    
    
    st.subheader(pleumorb_baja)
    st.subheader(p_leumoralta_res)
    
    
    con=sqlite3.connect('DB.db')
    con.row_factory=lambda Cursor,row:row[0]
    cur=con.cursor()
    
     #superv 
    leu_superv=cur.execute('SELECT AVG(Leupreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Leupreqx!=0)')
    leusuperv_res=cur.fetchone()
    
     #Mort leu 
    leu_mort=cur.execute('SELECT AVG(Leupreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Leupreqx!=0)')
    leumort_res=cur.fetchone()
    
    #p mort leu
    p_leu_superv=cur.execute('SELECT Leupreqx FROM Basecxcol WHERE (Comppostqx!="V") AND (Leupreqx!=0)')
    p_leu_superv_res=cur.fetchall()
    st.success(p_leu_superv_res)
    st.info(stats.shapiro(p_leu_superv_res))
    
    p_leu_mort=cur.execute('SELECT Leupreqx FROM Basecxcol WHERE (Comppostqx="V") AND (Leupreqx!=0)')
    p_leumort_res=cur.fetchall()
    st.success(p_leumort_res)
    st.info(stats.shapiro(p_leumort_res))
    
    p_mort_leu=stats.mannwhitneyu(p_leu_superv_res,p_leumort_res)
    st.error(p_mort_leu)

    
    
    
    
    
    
     #ADE prequirúrgica
    #morbilidad baja
    ADE_morb_baja=cur.execute('SELECT AVG(ADEpreqx)FROM Basecxcol WHERE (ADEpreqx!=0) AND (Comppostqx="I") OR (Comppostqx="II" AND ADEpreqx!=0)')
    ADEmorbaja_res=cur.fetchone()
    #Morb alta
    ADE_morb_alta=cur.execute('SELECT AVG(ADEpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (ADEpreqx!=0)')
    ADEmoralta_res=cur.fetchone()
    
    #p_ADE_ morb
    p_ADE_morb_baja=cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE (ADEpreqx!=0 AND Comppostqx="I") OR (Comppostqx="II" AND ADEpreqx!=0) ')
    p_ADEmorbaja_res=cur.fetchall()
    st.subheader(p_ADEmorbaja_res)
    #Morb alta
    p_ADE_morb_alta=cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE  (ADEpreqx!=0 AND Comppostqx="III") OR (Comppostqx="IV" AND ADEpreqx!=0) ')
    p_ADEmoralta_res=cur.fetchall()
    st.subheader(p_ADEmoralta_res)
    
    p_shapiro_morbaja=stats.shapiro(p_ADEmorbaja_res)
    st.warning(p_shapiro_morbaja)
    
    p_shapiro_morb_alta=stats.shapiro(p_ADEmoralta_res)
    st.error(p_shapiro_morb_alta)
    
     #superv 
    ade_superv=cur.execute('SELECT AVG(ADEpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (ADEpreqx!=0)')
    ADEsuperv_res=cur.fetchone()
    
     #Mort ade 
    ADE_mort=cur.execute('SELECT AVG(ADEpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (ADEpreqx!=0)')
    ADEmort_res=cur.fetchone()
    
    
      #HTO prequirúrgica
    #morbilidad baja
    HTO_morb_baja=cur.execute('SELECT AVG(HTOpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (HTOpreqx!=0)')
    HTOmorbaja_res=cur.fetchone()
    #Morb alta
    HTO_morb_alta=cur.execute('SELECT AVG(HTOpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (HTOpreqx!=0)')
    HTOmoralta_res=cur.fetchone()
    
     #superv 
    HTO_superv=cur.execute('SELECT AVG(HTOpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (HTOpreqx!=0)')
    HTOsuperv_res=cur.fetchone()
    
     #Mort ade 
    HTO_mort=cur.execute('SELECT AVG(HTOpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (HTOpreqx!=0)')
    HTOmort_res=cur.fetchone()
    
    
    
    
    
      #plaquetas prequirúrgica
    #morbilidad baja
    PLT_morb_baja=cur.execute('SELECT AVG(Plaqpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Plaqpreqx!=0)')
    PLTmorbaja_res=cur.fetchone()
    #Morb alta
    PLT_morb_alta=cur.execute('SELECT AVG(Plaqpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Plaqpreqx!=0)')
    PLTmoralta_res=cur.fetchone()
    
     #superv 
    PLT_superv=cur.execute('SELECT AVG(Plaqpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Plaqpreqx!=0)')
    PLTsuperv_res=cur.fetchone()
    
     #Mort ade 
    PLT_mort=cur.execute('SELECT AVG(Plaqpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Plaqpreqx!=0)')
    PLTmort_res=cur.fetchone()
    
     
     
     
      #AST prequirúrgica
    #morbilidad baja
    AST_morb_baja=cur.execute('SELECT AVG(ASTpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (ASTpreqx!=0)')
    ASTmorbaja_res=cur.fetchone()
    #Morb alta
    AST_morb_alta=cur.execute('SELECT AVG(ASTpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (ASTpreqx!=0)')
    ASTmoralta_res=cur.fetchone()
    
     #superv 
    AST_superv=cur.execute('SELECT AVG(ASTpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (ASTpreqx!=0)')
    ASTsuperv_res=cur.fetchone()
    
     #Mort ast 
    AST_mort=cur.execute('SELECT AVG(ASTpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (ASTpreqx!=0)')
    ASTmort_res=cur.fetchone()
     
     
     
     
      #ALT prequirúrgica
    #morbilidad baja
    ALT_morb_baja=cur.execute('SELECT AVG(ALTpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (ALTpreqx!=0)')
    ALTmorbaja_res=cur.fetchone()
    #Morb alta
    ALT_morb_alta=cur.execute('SELECT AVG(ALTpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (ALTpreqx!=0)')
    ALTmoralta_res=cur.fetchone()
    
     #superv 
    ALT_superv=cur.execute('SELECT AVG(ALTpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (ALTpreqx!=0)')
    ALTsuperv_res=cur.fetchone()
    
     #Mort alt 
    ALT_mort=cur.execute('SELECT AVG(ALTpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (ALTpreqx!=0)')
    ALTmort_res=cur.fetchone()
    
    
    
     #Bil prequirúrgica
    #morbilidad baja
    BIL_morb_baja=cur.execute('SELECT AVG(Biltotpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Biltotpreqx!=0)')
    BILmorbaja_res=cur.fetchone()
    #Morb alta
    BIL_morb_alta=cur.execute('SELECT AVG(Biltotpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Biltotpreqx!=0)')
    BILmoralta_res=cur.fetchone()
    
     #superv 
    BIL_superv=cur.execute('SELECT AVG(Biltotpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Biltotpreqx!=0)')
    BILsuperv_res=cur.fetchone()
    
     #Mort bil 
    BIL_mort=cur.execute('SELECT AVG(Biltotpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Biltotpreqx!=0)')
    BILmort_res=cur.fetchone()
    
    
    
     #INR prequirúrgica
    #morbilidad baja
    INR_morb_baja=cur.execute('SELECT AVG(INRpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (INRpreqx!=0)')
    INRmorbaja_res=cur.fetchone()
    #Morb alta
    INR_morb_alta=cur.execute('SELECT AVG(INRpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (INRpreqx!=0)')
    INRmoralta_res=cur.fetchone()
    
     #superv 
    INR_superv=cur.execute('SELECT AVG(INRpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (INRpreqx!=0)')
    INRsuperv_res=cur.fetchone()
    
     #Mort bil 
    INR_mort=cur.execute('SELECT AVG(INRpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (INRpreqx!=0)')
    INRmort_res=cur.fetchone()
    
    
     #CREAT prequirúrgica
    #morbilidad baja
    CRE_morb_baja=cur.execute('SELECT AVG(Creatpreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Creatpreqx!=0)')
    CREmorbaja_res=cur.fetchone()
    #Morb alta
    CRE_morb_alta=cur.execute('SELECT AVG(Creatpreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Creatpreqx!=0)')
    CREmoralta_res=cur.fetchone()
    
     #superv 
    CRE_superv=cur.execute('SELECT AVG(Creatpreqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Creatpreqx!=0)')
    CREsuperv_res=cur.fetchone()
    
     #Mort bil 
    CRE_mort=cur.execute('SELECT AVG(Creatpreqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Creatpreqx!=0)')
    CREmort_res=cur.fetchone()
     
     
     
     #Tiempo de evolución
    #morbilidad baja
    TEv_morb_baja=cur.execute('SELECT AVG(Tiempoinsintqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Tiempoinsintqx!=0)')
    TEVmorbaja_res=cur.fetchone()
    #Morb alta
    TEV_morb_alta=cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Tiempoinsintqx!=0)')
    TEVmoralta_res=cur.fetchone()
    
     #superv 
    TEV_superv=cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Tiempoinsintqx!=0)')
    TEVsuperv_res=cur.fetchone()
    
     #Mort bil 
    TEV_mort=cur.execute('SELECT AVG(Tiempoinsintqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Tiempoinsintqx!=0)')
    TEVmort_res=cur.fetchone()
    
    
     #Tiempo quirúrgico
    #morbilidad baja
    Tqx_morb_baja=cur.execute('SELECT AVG(Duracionqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II") AND (Duracionqx!=0)')
    Tqxmorbaja_res=cur.fetchone()
    #Morb alta
    Tqx_morb_alta=cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV") AND (Duracionqx!=0)')
    Tqxmoralta_res=cur.fetchone()
    
     #superv 
    Tqx_superv=cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE (Comppostqx!="V") AND (Duracionqx!=0)')
    Tqxsuperv_res=cur.fetchone()
    
     #Mort bil 
    Tqx_mort=cur.execute('SELECT AVG(Duracionqx) FROM Basecxcol WHERE (Comppostqx="V") AND (Duracionqx!=0)')
    Tqxmort_res=cur.fetchone()
    
    
    
    #qSOFA
    #morbilidad baja
    qSOFA_morb_baja=cur.execute('SELECT AVG(qSOFApreqx)FROM Basecxcol WHERE (Comppostqx="I") OR (Comppostqx="II")')
    qSOFAmorbaja_res=cur.fetchone()
    #Morb alta
    qSOFA_morb_alta=cur.execute('SELECT AVG(qSOFApreqx) FROM Basecxcol WHERE (Comppostqx="III") OR (Comppostqx="IV")')
    qSOFAmoralta_res=cur.fetchone()
    
     #superv 
    qSOFA_superv=cur.execute('SELECT AVG(qSOFApreqx) FROM Basecxcol WHERE (Comppostqx!="V") ')
    qSOFAsuperv_res=cur.fetchone()
    
     #Mort bil 
    qSOFA_mort=cur.execute('SELECT AVG(qSOFApreqx) FROM Basecxcol WHERE (Comppostqx="V") ')
    qSOFAmort_res=cur.fetchone()
    
    
    data_bioquimico=[(leumorbaja_res,leumoralta_res,leusuperv_res,leumort_res),
                     (ADEmorbaja_res,ADEmoralta_res,ADEsuperv_res,ADEmort_res),
                     (HTOmorbaja_res,HTOmoralta_res,HTOsuperv_res,HTOmort_res),
                     (PLTmorbaja_res,PLTmoralta_res,PLTsuperv_res,PLTmort_res),
                     (ASTmorbaja_res,ASTmoralta_res,ASTsuperv_res,ASTmort_res),
                     (ALTmorbaja_res,ALTmoralta_res,ALTsuperv_res,ALTmort_res),
                     (BILmorbaja_res,BILmoralta_res,BILsuperv_res,BILmort_res),
                     (INRmorbaja_res,INRmoralta_res,INRsuperv_res,INRmort_res),
                     (CREmorbaja_res,CREmoralta_res,CREsuperv_res,CREmort_res),
                     (TEVmorbaja_res,TEVmoralta_res,TEVsuperv_res,TEVmort_res),
                     (Tqxmorbaja_res,Tqxmoralta_res,Tqxsuperv_res,Tqxmort_res),
                     (qSOFAmorbaja_res,qSOFAmoralta_res,qSOFAsuperv_res,qSOFAmort_res)]
    indexbioquimi=['Leucocitosis','ADE','Hematocrito','Plaquetas mm3','AST mg/dl','ALT mg/dl','Bilirrubina total mg/dl','INR','Creatinina mg/dl','Tiempo de evolución (días)',
                   'Tiempo de cirugía(minutos)','qSOFA']
    columnas_bioquimica=['CD I y II','CD III y IV','Supervivientes','Mortalidad']
    df_bioquimica=pd.DataFrame(data_bioquimico,indexbioquimi,columnas_bioquimica)
    st.table(df_bioquimica)
    
    
    
    
    
def tablano8():
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    
    #Patología vesicular de inicio
    col_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%[]%" ) AND (Comppostqx="I" OR Comppostqx="II")' )
    colnomor_res,=cur.fetchone()
    
    col_simorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%[]%" ) AND (Comppostqx="III" OR Comppostqx="IV")' )
    colsimor_res,=cur.fetchone()
    
    col_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%[]%" ) AND (Comppostqx="V")' )
    colmorta_res,=cur.fetchone()
    
    
    #infarto agudo al miocardio con morbilidad baja
    iam_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Infarto%" OR PRoccardio LIKE "%Cateterismo%") AND (Comppostqx="I" OR Comppostqx="II")' )
    iamnomor_res,=cur.fetchone()
    
    iam_simorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Infarto%" OR PRoccardio LIKE "%Cateterismo%") AND (Comppostqx="III" OR Comppostqx="IV")' )
    iamsimor_res,=cur.fetchone()
    
    iam_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Infarto%" OR PRoccardio LIKE "%Cateterismo%") AND (Comppostqx="V")' )
    iammorta_res,=cur.fetchone()
    
    
     #Arritmia
    arritmia_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%marcapaso%" ) AND (Comppostqx="I" OR Comppostqx="II")' )
    arritmia_nomor_res,=cur.fetchone()
    
    arritmia_simorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%marcapaso%") AND (Comppostqx="III" OR Comppostqx="IV")' )
    arritmia_simor_res,=cur.fetchone()
    
    arritmia_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%marcapaso%") AND (Comppostqx="V")' )
    arritmia_morta_res,=cur.fetchone()
    
    
    
    #Cirugía
    cirugía_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Cirugia%" OR PRoccardio Like "%Reemplazo%") AND (Comppostqx="I" OR Comppostqx="II")' )
    cx_nomor_res,=cur.fetchone()
    
    cx_simorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Cirugia%" OR PRoccardio Like "%Reemplazo%") AND (Comppostqx="III" OR Comppostqx="IV")' )
    cx_simor_res,=cur.fetchone()
    
    cx_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%Cirugia%" OR PRoccardio Like "%Reemplazo%") AND (Comppostqx="V")' )
    cx_morta_res,=cur.fetchone()
    
    
    #ICC
    IC_nomorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%funcional%" ) AND (Comppostqx="I" OR Comppostqx="II")' )
    IC_nomor_res,=cur.fetchone()
    
    IC_simorb=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%funcional%") AND (Comppostqx="III" OR Comppostqx="IV")' )
    IC_simor_res,=cur.fetchone()
    
    IC_mort=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE (PRoccardio LIKE "%funcional%" ) AND (Comppostqx="V")' )
    IC_morta_res,=cur.fetchone()
    
    
    
    
    data_motivingreso=[(colnomor_res,(colnomor_res/18*100),colsimor_res,(colsimor_res/18*100),colmorta_res,(colmorta_res/18*100)),(iamnomor_res,(iamnomor_res/18*100),iamsimor_res,(iamsimor_res/18*100),iammorta_res,(iammorta_res/18*100)),(arritmia_nomor_res,(arritmia_nomor_res/18*100),arritmia_simor_res,(arritmia_simor_res/18*100),arritmia_morta_res,(arritmia_morta_res/18*100)),(cx_nomor_res,(cx_nomor_res/18*100),cx_simor_res,(cx_simor_res/18*100),cx_morta_res,(cx_morta_res/18*100)),
                       (IC_nomor_res,(IC_nomor_res/18*100),IC_simor_res,(IC_simor_res/18*100),IC_morta_res,(IC_morta_res/18*100))]    
    index_motvingreso=['Colecistitis aguda','Infarto agudo al miocardio','Arritmia','Cirugía cardiovascular','Insuficiencia cardiáca']
    col_motinvgreso=['CD I y II',"CD <II%",'CD III y IV'," CD>III %",'Mortalidad',"%"]
    
    df_motvingreso=pd.DataFrame(data_motivingreso,index_motvingreso,col_motinvgreso)
    st.table(df_motvingreso)
    

  
  