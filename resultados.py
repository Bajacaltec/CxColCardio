from turtle import pensize, width
import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
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
    gencol=['Género']
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    dx=pd.DataFrame(df,ind,columns=(gencol))
    col1,col2=st.columns(2)
    with col1:
        st.table(dx)
    with col2:
        st.bar_chart(dx)

def antropometrico():
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    edaf=cur.execute('''SELECT avg(Edad) FROM Basecxcol''')
    ed=edaf.fetchall()
    edas,=ed
    edafe,=edas
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    pes=cur.execute('''SELECT avg(Peso) FROM Basecxcol''')
    peso,=pes.fetchall()
    pas,=peso
    tall=cur.execute('''SELECT avg(Talla) FROM Basecxcol''')
    talle,=tall.fetchall()
    telle,=talle
    imcbis=cur.execute('''SELECT avg(IMC) FROM Basecxcol''')
    imc,=imcbis.fetchall()
    imcfin,=imc
    
    # ---------------------------------------------------------------------------- #
    #                                  Tabaquismo                                  #
    # ---------------------------------------------------------------------------- #
    #Resultados tabaquismo
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    tab=cur.execute('''SELECT COUNT(*) FROM Prueba9 WHERE Tabaquismo = 'Si' ''')
    tabsi,=tab.fetchone()
    tabnosc=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo = 'No' ''')
    tabno,=tab.fetchone()
    tabtotal=tabsi+tabno
    #porcentaje de pacientes que consumen tabaco
    tabporcentaje=tabsi/tabtotal*100
    
    cajetillas=cur.execute('''SELECT avg(Cajetillas) FROM Basecxcol''')
    caje,=cajetillas.fetchall()
    caj,=caje
    
    
    
    # tabla principal
    
    # Create the index
    st.subheader('Biométricos')
    
    columna=['Peso','Talla','IMC'] # nombre de las
    df = pd.DataFrame({'Edad':[edafe,telle],'Peso':[pas,telle], #nombre y valores de los datos, al poner dos variables se ponen dos filas
                   'Talla':[telle,imcfin],
                   'IMC':[imcfin,pas],'Tabaquismo':[tabporcentaje,pas],'Cajetillas':[caj,telle]})
    # Print the DataFrame
    index_ = ['Promedio','index'] # nombre de las filas
    
    # Set the index
    df.index = index_ # adjudicar el index
    st.table(df)
    
    
    
    # ---------------------------------------------------------------------------- #
    #           Uso de vasopresores como desencadenantes de la enfermedad          #
    # ---------------------------------------------------------------------------- #
    
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    vas=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores LIKE '%Si%' ''')
    vasopresi=vas.fetchone()
    
    vasno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores LIKE '%No%' ''')
    vasopresno=vasno.fetchone()
    
    st.subheader('Vasopresores')
    
    vasopresi_count = [vasopresi,vasopresno]
    vasopres_index=['Uso de vasopresor','Sin vasopresor']
    columna_vasopresor=['N']
    df_vasopres=pd.DataFrame(vasopresi_count,vasopres_index,columna_vasopresor)
    col1,col2=st.columns(2)
    with col1:
        st.table(df_vasopres)
    with col2:
        st.bar_chart(df_vasopres,15,250,)
   
    
    
    # ---------------------------------------------------------------------------- #
    #                                 Antecedentes                                 #
    # ---------------------------------------------------------------------------- #
    
    #comorbilidades
    
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    
    #El LIKE sirve para buscar algo que se parece en el STRING de la base de datos
    crondm=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Diabetes%' """)
    DMcount=crondm.fetchone()
    
    crondm=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Hipertensión%' """)
    HAScount=crondm.fetchone()
    
    valvcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Valvulopatia%' """)
    valvcount=crondm.fetchone()
    
    IAMcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Infarto%' """)
    IAMcount=crondm.fetchone()
    
    crónicos_todo=[DMcount,HAScount,valvcount,IAMcount]
    indexcronicos=['Diabetes mellitus','Hipertensión arterial','Valvulopatia','IAM']
    columnas_comor=['N']
    dfcrónicos=pd.DataFrame(crónicos_todo,indexcronicos,columnas_comor)
    

    
    st.subheader('Comorbilidades')
    st.table(dfcrónicos)
    st.line_chart(dfcrónicos,50,200)

    


   # ---------------------------------------------------------------------------- #
   #                        Procedimiendos cardiovasculares                       #
   # ---------------------------------------------------------------------------- #
    
    #Procedimientos cardiovasculares, conteo de procedimientos
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    prcardio=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Proccardio LIKE '%cirugia cardiovascular%' ''')
    procedcardio=prcardio.fetchone()
    
    cat_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Proccardio LIKE '%Cateterismo%' ''')
    procateter=cat_count.fetchone()
    
    proc_cardiovasculares=[procedcardio,procateter]
    proccardio_index=['Cirugía cardiovascular','Cateterismo']
    col_procardio=['N']
    df_proccardio=pd.DataFrame(proc_cardiovasculares,proccardio_index,col_procardio)
    st.subheader('Procedimientos cardiovasculares')
    st.table(df_proccardio)
    st.line_chart(df_proccardio,50,200)

    
    # ---------------------------------------------------------------------------- #
    #                                  Tabaquismo                                  #
    # ---------------------------------------------------------------------------- #
    #tabaquismo
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    tabno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo = 'No' ''')
    tabneg=tabno.fetchone()
    
    tabsi=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tabaquismo = 'Si' ''')
    tabpos=tabsi.fetchone()
    
    dftab=[tabneg,tabpos]
    tab_index=['Tabaquismo positivo','Tabaquismo negativo']
    col_tab=['N']
    df_tab=pd.DataFrame(dftab,tab_index,col_tab)
    
    st.subheader('Tabaquismo')
    st.table(df_tab)
    st.area_chart(df_tab,50,200)

    
    #vasopres = pd.DataFrame({'Uso de vasopresores':[vasopres]})
    # Print the DataFrame
    #indice = ['Promedio'] # nombre de las filas
    
    # Set the index
   # vasopres.index = indice # adjudicar el index
    #st.dataframe(vasopres)
    
    
    # ---------------------------------------------------------------------------- #
    #                             Ventilación mecánica                             #
    # ---------------------------------------------------------------------------- #
    #pacientes con ventilación preqx y número de días
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    ventmecpeqxsi=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Diasventmec != 0 ''')
    ventcountpreqxsi,=ventmecpeqxsi.fetchone()
    ventmecpeqxno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Diasventmec = 0 ''')
    ventcountpreqxno,=ventmecpeqxno.fetchone()
    st.subheader('Pacientes con ventilación mecánica prequirúrgica')
    ventmec_promedio=(ventcountpreqxsi/(ventcountpreqxsi+ventcountpreqxno))*100

    ventdf=[ventcountpreqxsi,ventcountpreqxno]
    ind=['Ventilación mecánica prequirúrgica','Sin ventilación mecánica']
    gencol=['Ventilación']
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    vent_df=pd.DataFrame(ventdf,ind,columns=gencol)
    dol1,dol2=st.columns(2)
    with dol1:
        st.table(vent_df)
    with dol2:
        st.bar_chart(vent_df)

    
    # ---------------------------------------------------------------------------- #
    #                      Uso de vasopresores prequirúrgicos                      #
    # ---------------------------------------------------------------------------- #
    
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    vasopreqx=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores = 'Si' ''')
    vasoprescount,=vasopreqx.fetchone()
    vasopreqxno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores = 'No' ''')
    vasoprescountno,=vasopreqxno.fetchone()
    st.subheader('Pacientes con vasopresores prequirúrgicos')
    promedio_vasopresores=(vasoprescount/(vasoprescount+vasoprescountno))*100
    vasopresdf=[vasoprescount,vasoprescountno,promedio_vasopresores]
    ind=['Vasopresores prequirúrgica','Sin vasopresores','Porcentaje de uso de vasopresores']
    gencol=['Vasopresores']
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    dx=pd.DataFrame(vasopresdf,ind,columns=gencol)
    st.table(dx)


# ---------------------------------------------------------------------------- #
#                         Tipo de vasopresor utilizado                         #
# ---------------------------------------------------------------------------- #

#Contar cual vasopresor es el más utilizado en el caso de los pacientes con vasopresores prequirúrvicos


# ---------------------------------------------------------------------------- #
#               Procedimiento quirúrgico más asociado con la CCLA              #
# ---------------------------------------------------------------------------- #
#Contar los procedimientos más comúnes en pacientes con CCLA
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    proccardio=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio = "['Cirugia cardiovascular']" ''')
    conteo_proccardio,=proccardio.fetchone()
    
    #Hasta aquí es para contar cirugía cardiovascular
    #Inicia cateterismo cardiaco
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    catcardio=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio = "['Cateterismo cardiaco']" ''')
    conteo_catcardio,=catcardio.fetchone()
    
    #####
   
    
    reemplazo_valvular=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio = "['Reemplazo valvular']" ''')
    remplazo_count,=reemplazo_valvular.fetchone()
    
# ---------------------------------------------------------------------------- #
#                        Procedimientos cardiovasculares                       #
# ---------------------------------------------------------------------------- #
 #Procedimientos cardiovasculares
    st.success('Procedimientos cardiovasculares')
    proccardiovasculares=(conteo_catcardio,conteo_catcardio,remplazo_count)
    indiceprocardio=['Cirugía cardiovascular','Cateterismo','Reemplazo valvular']
    procardio_columnas=['Procedimientos']
    dfprocardio=pd.DataFrame(proccardiovasculares,indiceprocardio,columns=procardio_columnas,)
    st.table(dfprocardio)
    st.line_chart(dfprocardio)
    
#Vitales de ingreso, valorar si hacer una tabla con puntos para ver como se distribuyen los vitales


#laboratorios de ingreso
#ADE


#SOFA

#Vasopresor postqx

#DIas en UCI postqx

#Síntomas compatibles con CCLA

    # ---------------------------------------------------------------------------- #
    #                               Hallazgos por USG                              #
    # ---------------------------------------------------------------------------- #
    #Hallazgos por USG
    con = sqlite3.connect('DB.db')
    cur = con.cursor()

    usg_liquidocount=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Líquido perivesicular%" ''')
    usg_liquido=usg_liquidocount.fetchone()

    usg_litoscount=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Litiasis%" ''')
    usg_litos=usg_litoscount.fetchone()

    usg_lodocount=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Lodo biliar%" ''')
    usg_lodo=usg_lodocount.fetchone()
    
    usg_paredcount=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Engrosamiento de pared%" ''')
    usg_pared=usg_paredcount.fetchone()
    
    usg_anatocount=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Anormalidad anatomíca%" ''')
    usg_anato=usg_anatocount.fetchone()
    
    
    hallazgos_usg=(usg_liquido, usg_litos,usg_lodo,usg_pared,usg_anato)
    usg_index=['Líquido perivesicular','Litiasis vesícular','Lodo biliar','Engrosamiento de pared','Anormalidad anatómica']
    col_usg=['Hallazgos ultrasonográficos']
    df_usg=pd.DataFrame(hallazgos_usg,usg_index,col_usg)
    df_usg.style.set_caption("Hello World")

    st.info('Hallazgos USG')
    st.table(df_usg)
    st.area_chart(df_usg)

    #ASA

    #Hallazgos tomografícos

    # ---------------------------------------------------------------------------- #
    #                                     Tokyo                                    #
    # ---------------------------------------------------------------------------- #
    tokyo_count_leve=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tokyo LIKE "%Leve%" ''')
    tokyo_leve=tokyo_count_leve.fetchone()
    
    tokyo_count_moderado=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tokyo LIKE "%Moderado%" ''')
    tokyo_moderado=tokyo_count_moderado.fetchone()
    
    tokyo_count_severo=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Tokyo LIKE "%Severo%" ''')
    tokyo_severo=tokyo_count_severo.fetchone()
    
    clas_tokyo=(tokyo_leve,tokyo_moderado,tokyo_severo)
    index_tokyo=['Leve','Moderado','Severo']
    tokyo_col=['Clasificación de Tokyo de severidad de CCLA']
    df_tokyo=pd.DataFrame(clas_tokyo,index_tokyo,tokyo_col)
    zol1,zol2=st.columns(2)
    with zol1:
        st.table(df_tokyo)
    with zol2:
        st.bar_chart(df_tokyo)
    

    #Laboratorios prequirúrgicos
    # ---------------------------------------------------------------------------- #
    #                              Inicio de síntomas                              #
    # ---------------------------------------------------------------------------- #
    #Tiempo de inicio de síntomas hasta cirugía
    tiempo_qxcount=cur.execute('''SELECT Tiempoinsintqx FROM Basecxcol ORDER BY DiasUCIposqx ASC  ''')
    tiempo_sintqx=tiempo_qxcount.fetchall()
    
    ADE_count=cur.execute('''SELECT ADEing FROM Basecxcol ''')
    ADEgr=ADE_count.fetchall()
    
    df_tiempo=(tiempo_sintqx)
    coluna=['Tiempo de inicio de síntomas']
    serie_tiempoqx=pd.DataFrame(tiempo_sintqx)
    st.info('Tiempo de inicio de síntomas a procedimiento quirúrgico/Dias UCI postqx')
    st.line_chart(serie_tiempoqx,)
    st.subheader(tiempo_sintqx)

    # ---------------------------------------------------------------------------- #
    #                                tipo de cirugía                               #
    # ---------------------------------------------------------------------------- #
    #Tipo de cirugía
    tipocxcount=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE tipoqx LIKE '%Laparoscopica%' """ )
    tipocx_laparos=tipocxcount.fetchone()
    
    tipocxcount_abierta=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE tipoqx LIKE '%Abierta%' """ )
    tipocx_abierta=tipocxcount.fetchone()
    
    conversion_cxcount=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Conversión = '1' """)
    conversion=conversion_cxcount.fetchone()
    
    tipocx=(tipocx_laparos,tipocx_abierta,conversion)
    index_tipocx=['Cirugía laparoscópica','Cirugía abierta','Cirugía convertida']
    col_tipocx=['Tipo de cirugía']
    df_tipocx=pd.DataFrame(tipocx,index_tipocx,col_tipocx)
    st.table(df_tipocx)
    st.bar_chart(df_tipocx)
    
    
    # ---------------------------------------------------------------------------- #
    #                              Duración de cirugía                             #
    # ---------------------------------------------------------------------------- #
    duracion_cx=cur.execute("""SELECT Duracionqx FROM Basecxcol  """ )
    duracioncx=duracion_cx.fetchall()
    st.info('Duración de cirugía')
    col_duracioncx=['Tiempo en minutos']
    #promedio_tiempo=cur.execute("""SELECT avg(Duracionqx) FROM Basecxcol""")
    #promediocx,=promedio_tiempo.fetchone()
    #df_duracioncx=[duracioncx]

    df_duracion=pd.DataFrame(duracioncx,columns=col_duracioncx)
    st.table(df_duracion)
    st.line_chart(df_duracion)
    #Conversión de cirugúa

    #Días de estancia 

    #Uso de vasopresor postquirúrgico

    #Complicaciones postquirúrgicas

#Ventilación mecánica postquirúrgica

#Dias uci postqx

#Recurrencia de síntomas

# ---------------------------------------------------------------------------- #
#                                  Mortalidad                                  #
# ---------------------------------------------------------------------------- #
#Mortalidad
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
   
    st.error('Mortalidad')
    mort_si=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Muerte = "Si" ''')
    Mort_count,=mort_si.fetchone()
    
    mort_no=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Muerte= "No" ''')
    Mort_countno,=mort_no.fetchone()
   
    porcentaje_mortalidad=(Mort_count/(Mort_count+Mort_countno))*100
    mortalidad=(Mort_count,Mort_countno,)
    Supervivencia_porcentaje=(Mort_countno/(Mort_count+Mort_countno))*100
    supervvsmort=(Supervivencia_porcentaje,porcentaje_mortalidad)
    index_mortalidad=('Defunciones','Pacientes vivos')
    index_supervivencia=('Supervivientes','Mortalidad')
    columnas_mortalidad=['Número de pacientes']
    df_mortalidad=pd.DataFrame(mortalidad,index_mortalidad,columnas_mortalidad)
    df_supervivencia=pd.DataFrame(supervvsmort,index_supervivencia,columnas_mortalidad)

    st.table(df_mortalidad)
    st.bar_chart(df_mortalidad)
    st.table(df_supervivencia)
    st.bar_chart(df_supervivencia)

