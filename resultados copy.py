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


        

def caracteristicas_base():
    con = sqlite3.connect('Basededatos.db')
    cur = con.cursor()
    masc=cur.execute('''SELECT COUNT(*) FROM Cxcolcardio WHERE Genero='Masculino' ''')
    masc_count,=cur.fetchone()
    
    fem=cur.execute('''SELECT COUNT(*) FROM Cxcolcardio WHERE Genero='Femenino' ''')
    fem_count,=cur.fetchone()
    

    
    

    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    serie_edad=cur.execute('SELECT Edad FROM Basecxcol')
    edad_seriada=cur.fetchall()
    avg_edad=cur.execute('SELECT AVG(Edad) FROM Basecxcol')
    avg_edad_count,=cur.fetchone()

    #indexserieedad=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
    #df_edad2=pd.DataFrame(edad_seriada,index=indexserieedad,columns=['Edad'])
    #st.bar_chart(df_edad2)
    #df_edad=pd.DataFrame({'Edad':edad_seriada,'Pacientes':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]})
    
    
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    #Serie de peso
    cur.execute('SELECT Peso FROM Basecxcol WHERE Peso != 1')
    peso=cur.fetchall()
    #Peso promedio
    cur.execute('SELECT AVG(Peso) FROM Basecxcol WHERE Peso != 1')
    peso_avg,=cur.fetchone()
    
    
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    cur.execute('SELECT Talla FROM Basecxcol WHERE Talla !=1')
    talla=cur.fetchall()
    
    cur.execute('SELECT AVG(Talla) FROM Basecxcol WHERE Talla !=1')
    talla_promedio,=cur.fetchone()
    
    IMC=cur.execute('SELECT AVG(IMC) FROM Basecxcol WHERE Peso!=1')
    IMC_avg,=cur.fetchone()
    
    
    
    
    
    
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
    tabporcentaje=tabsi/tabtotal*100
    cajetillas=cur.execute('''SELECT avg(Cajetillas) FROM Basecxcol''')
    caje,=cajetillas.fetchall()
    caj,=caje
    
   
    
    
    # ---------------------------------------------------------------------------- #
    #           Uso de vasopresores como desencadenantes de la enfermedad          #
    # ---------------------------------------------------------------------------- #
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    vas=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores LIKE '%Si%' ''')
    vasopresi=vas.fetchone()
    
    vasno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores LIKE '%No%' ''')
    vasopresno=vasno.fetchone()
    
    
    vasopresi_count = [vasopresi,vasopresno]
    vasopres_index=['Uso de vasopresor','Sin vasopresor']
    columna_vasopresor=['N']
    
   
   
    
    
    # ---------------------------------------------------------------------------- #
    #                                 Antecedentes                                 #
    # ---------------------------------------------------------------------------- #
    
    #comorbilidades
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    
    #El LIKE sirve para buscar algo que se parece en el STRING de la base de datos
    crondm=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Diabetes%' """)
    global DMcount
    DMcount,=crondm.fetchone()
    
    crondm=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Hipertensión%' """)
    HAScount,=crondm.fetchone()
    
    valvcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Valvulopatia%'  """)
    valvcount,=crondm.fetchone()
    
    IAMcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Infarto%' """)
    IAMcount,=crondm.fetchone()
    
    ICCcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Insuficiencia cardiaca%' """)
    ICCcount,=cur.fetchone()
    
    EVCcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%Evento vascular cerebral%' """)
    EVCcount,=cur.fetchone()
    
    EPOCcomor=cur.execute("""SELECT COUNT(*) FROM Basecxcol WHERE Crónicos LIKE '%EPOC%' """)
    EPOCcount,=cur.fetchone()
    global crónicos_todo
    crónicos_todo=[DMcount,HAScount,valvcount,IAMcount,ICCcount,EVCcount,EPOCcount]
    global indexcronicos
    indexcronicos=['Diabetes mellitus','Hipertensión arterial','Valvulopatia','IAM','Insuficiencia cardiáca','EVC','EPOC']

    df_crónicos=pd.DataFrame({'Crónicos':['Diabetes mellitus','Hipertensión arterial','Valvulopatia','IAM','Insuficiencia cardiáca','EVC','EPOC'],'Enfermedades':[DMcount,HAScount,valvcount,IAMcount,ICCcount,EVCcount,EPOCcount]})
    #lu=alt.Chart(df_crónicos).mark_bar(size=30).encode(
    #x=alt.X('Enfermedades', axis=alt.Axis(labels=True),title=None),
    #y=alt.Y('Crónicos', axis=alt.Axis(labels=True),title=None),
    #color=alt.Color('Enfermedades',legend=None)).properties(width=1200,height=400).configure_axis(labelFontSize=18,titleFontSize=20).interactive()
    
    #st.altair_chart(lu)
    #st.info('Las comorbilidades más frecuentementemente encontradas se asocian a factores de riesgo clásicos para enfermedades cardiovasculares, el antecedente más relevante después de estos es el infarto agudo al miocardio')

  
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
    ventmec_promedio=(ventcountpreqxsi/(ventcountpreqxsi+ventcountpreqxno))*100

    

    
    # ---------------------------------------------------------------------------- #
    #                      Uso de vasopresores prequirúrgicos                      #
    # ---------------------------------------------------------------------------- #
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
    vasopreqx=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores = 'Si' ''')
    vasoprescount,=vasopreqx.fetchone()
    vasopreqxno=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Vasopresores = 'No' ''')
    vasoprescountno,=vasopreqxno.fetchone()
    promedio_vasopresores=(vasoprescount/(vasoprescount+vasoprescountno))*100
    vasopresdf=[vasoprescount,vasoprescountno,promedio_vasopresores]
    ind=['Vasopresores prequirúrgica','Sin vasopresores','Porcentaje de uso de vasopresores']
    gencol=['Vasopresores']
    #Para el index se requiere dar una lista para asignarlo al pandas df, y en la gráfica
    dx=pd.DataFrame(vasopresdf,ind,columns=gencol)


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
    
    det_IAM=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE '%Infarto agudo al miocardio%' ''')
    det_IAM_count,=cur.fetchone()
    
    det_cxcardio=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE '%Cirugia cardiovascular%' ''')
    det_cxcardio_count,=cur.fetchone()
    
    det_rempvalv=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE PRoccardio LIKE '%Reemplazo valvular%' ''')
    det_rempvalv_count,=cur.fetchone()
    
    
    #desencad=[conteo_catcardio,det_IAM_count,det_cxcardio_count,det_rempvalv_count]
    #index_desencad=['Cateterismo','Infarto agudo al miocardio','Cirugía cardiovascular','Reemplazo valvular']
    #df_desencad=pd.DataFrame({'# Casos':desencad,'Procedimientos':index_desencad} )
    #f=alt.Chart(df_desencad).mark_bar().encode(
    #x=alt.X('# Casos'),
    #y=alt.Y('Procedimientos'),
    #color='# Casos').properties(width=900,height=350).configure_axis(labelFontSize=15,titleFontSize=25).interactive().interactive()
    #st.altair_chart(f,use_container_width=True)
    # ---------------------------------------------------------------------------- #
    #                                Vitales ingreso                               #
    # ---------------------------------------------------------------------------- #
#Vitales de ingreso, valorar si hacer una tabla con puntos para ver como se distribuyen los vitales
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    vitales_ingreso=cur.execute('''SELECT FCing,FRing,Sising,Diasing,Temping FROM Basecxcol  ''')
    vitales_ingreso_count=cur.fetchall()
   
#laboratorios de ingreso
# ---------------------------------------------------------------------------- #
#                            Marcadores bioquímicos de ingreso                       #
# ---------------------------------------------------------------------------- #
    ADE_count_ing=cur.execute('SELECT ADEing FROM Basecxcol WHERE ADEing!=1 AND ADEing!=0')
    ade_count_fecht_ing=cur.fetchall()
    
    leu_count_ing=cur.execute('SELECT avg(Leuing) FROM Basecxcol WHERE Leuing!=0')
    leufechting,=cur.fetchone()
    
    AST_coun=cur.execute('SELECT avg(ASTing) FROM Basecxcol WHERE ASTing!=0')
    asting_fetch,=cur.fetchone()
    
    ALT_count=cur.execute('SELECT avg(ALTing) FROM Basecxcol WHERE ALTing!=0')
    alting_fecht,=cur.fetchone()
    
    Biltot_ing_count=cur.execute('SELECT avg(Biltoting) FROM Basecxcol WHERE Biltoting!=1')
    biltoting_fetch,=cur.fetchone()
    
    FA_ing_count=cur.execute('SELECT avg(FAing) FROM Basecxcol WHERE FAing!=0')
    fa_fetch,=cur.fetchone()
    
    INR_ing_count=cur.execute('SELECT avg(INRing) FROM Basecxcol WHERE INRing !=1')
    inring_fetch,=cur.fetchone()
    
    Naing_coount=cur.execute('SELECT avg(Naing) FROM Basecxcol WHERE Naing!=1')
    naing_fetch,=cur.fetchone()
    
    K_ing=cur.execute('SELECT avg(King) FROM Basecxcol WHERE King!=0')
    king_fetch,=cur.fetchone()
    
    phing_count=cur.execute('SELECT avg(PHing) FROM Basecxcol WHERE PHing!=0')
    phing_fetch,=cur.fetchone()
    
    htoing_count=cur.execute('SELECT avg(Hematocritoing) FROM Basecxcol WHERe Hematocritoing!=1')
    htoing_fetch,=cur.fetchone()
    
   
    
#Marcadores bioquimicos prequirúrgico
    ADE_count_preqx=cur.execute('SELECT ADEpreqx FROM Basecxcol WHERE ADEpreqx!=1 AND ADEpreqx!=0')
    ade_count_fecht_preqx=cur.fetchall()
    
    st.dataframe(ade_count_fecht_preqx)
    
    leu_count_preqx=cur.execute('SELECT avg(Leupreqx) FROM Basecxcol WHERE Leupreqx!=0')
    leufechpreqx,=cur.fetchone()
    
    AST_coun_preqx=cur.execute('SELECT avg(ASTpreqx) FROM Basecxcol WHERE ASTpreqx!=0')
    astpreqx_fetch,=cur.fetchone()
    
    ALT_count_preqx=cur.execute('SELECT avg(ALTpreqx) FROM Basecxcol WHERE ALTpreqx!=0')
    altpreqx_fecht,=cur.fetchone()
    
    Biltot_preqx_count=cur.execute('SELECT avg(Biltotpreqx) FROM Basecxcol WHERE Biltotpreqx!=1')
    biltotpreqx_fetch,=cur.fetchone()
    
    FA_preqx_count=cur.execute('SELECT avg(FApreqx) FROM Basecxcol WHERE FApreqx!=0')
    fa_fetch_preqx,=cur.fetchone()
    
    INR_preqx_count=cur.execute('SELECT avg(INRpreqx) FROM Basecxcol WHERE INRpreqx !=1')
    inr_fetch_preqx,=cur.fetchone()
    
    Napreqx_coount=cur.execute('SELECT avg(NApreqx) FROM Basecxcol WHERE NApreqx!=1')
    napreqx_fetch,=cur.fetchone()
    
    K_preqx=cur.execute('SELECT avg(Kpreqx) FROM Basecxcol WHERE Kpreqx!=0')
    kpreqx_fetch,=cur.fetchone()
    
    phpreqx_count=cur.execute('SELECT avg(PHpreqx) FROM Basecxcol WHERE PHpreqx!=0')
    phpreqx_fetch,=cur.fetchone()
    
    htopreqx_count=cur.execute('SELECT avg(HTOpreqx) FROM Basecxcol WHERe HTOpreqx!=1')
    htopreqx_fetch,=cur.fetchone()
    
    ttADE = stats.ttest_ind(ade_count_fecht_ing, ade_count_fecht_preqx, 
                      equal_var=True)

     
    marc_bioquimicos=[ade_count_fecht_ing,ade_count_fecht_preqx],[leufechting,leufechpreqx],[asting_fetch,astpreqx_fetch],[alting_fecht,altpreqx_fecht],[biltoting_fetch,biltotpreqx_fetch],[fa_fetch,fa_fetch_preqx],[inring_fetch,inr_fetch_preqx],[naing_fetch,napreqx_fetch],[king_fetch,kpreqx_fetch],[phing_fetch,phpreqx_fetch],[htoing_fetch,htopreqx_fetch]
    index_bioquimico_ing=['ADE','Leucocitos','AST','ALT','Bilirrubina total','Fosfatasa alcalina','INR','Sodio sérico','Potasio sérico','pH',
                          'Hematocrito']
    column_bioquimio_ing=['Ingreso','Prequirúrgicos']
    
    
    
    Df_bioquimico=pd.DataFrame(marc_bioquimicos,index=index_bioquimico_ing,columns=column_bioquimio_ing)
    #st.dataframe(Df_bioquimico)
#ADE


#SOFA

#Vasopresor postqx

#DIas en UCI postqx
# ---------------------------------------------------------------------------- #
#                               sintomas de ccla                               #
# ---------------------------------------------------------------------------- #
#Síntomas compatibles con CCLA
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    dolor_hipodere=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%hipocondrio%" ''')
    dolorhipodere_count,=cur.fetchone()
    
    Nausea_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Nausea%" ''')
    nausea_count,=cur.fetchone()
    
    Murphy_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Murphy%" ''')
    Murphy_count,=cur.fetchone()
    
    icter_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Ictericia%" ''')
    icter_count,=cur.fetchone()
    
    vespalpable_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Palpable%" ''')
    vespalpable_count,=cur.fetchone()
    
    difuso_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Difuso%" ''')
    difuso_count,=cur.fetchone()
    
    fiebre_sint=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Sintomascompatccla LIKE "%Fiebre%" ''')
    fiebre_count,=cur.fetchone()
    xe=[0,100]
    dolordf=[dolorhipodere_count,nausea_count,Murphy_count,icter_count,vespalpable_count,difuso_count,fiebre_count]
    dolordf_index=['Dolor en hipocondrio derecho','Nausea','Signo de Murphy','Ictericia','Vesícula palpable','Dolor abdominal generalizado','Fiebre']
    df_sintomasccla=pd.DataFrame({'Síntomas':['Dolor en hipocondrio derecho','Nausea y vómito','Signo de Murphy','Ictericia','Vesícula palpable','Dolor abdominal difuso','Fiebre'],
                                  '# Pacientes':[dolorhipodere_count,nausea_count,Murphy_count,icter_count,vespalpable_count,difuso_count,fiebre_count
        ],})
    l=alt.Chart(df_sintomasccla).mark_bar(size=65).encode(
    x=alt.X('# Pacientes', axis=alt.Axis(labels=True),title=None
),
    y=alt.Y('Síntomas', axis=alt.Axis(labels=True)),
    color=alt.Color('Síntomas',legend=None)).properties(width=500,height=400).configure_axis(labelFontSize=18,titleFontSize=20).interactive()
    #st.altair_chart(l,use_container_width=True)
    #st.info('Los síntomas más comúnes presentes en el padecimiento actual de pacientes con enfermedades cardiovasculares que presentan sintomatología asociada a cuadros de colecistitis aguda')

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
    
    usg_dist=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Distensión vesicular%" ''')
    usg_dist_count=cur.fetchone()
    
    usg_dilvb=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Hallazusg LIKE "%Dilatación de vía biliar%" ''')
    usg_dilvb_count=cur.fetchone()
    
    
    hallazgos_usg=(usg_liquido, usg_litos,usg_lodo,usg_pared,usg_anato,usg_dist_count,usg_dilvb_count)
    usg_index=['Líquido perivesicular','Litiasis vesícular','Lodo biliar','Engrosamiento de pared','Anormalidad anatómica','Hidrocolecisto','Dilatación de vía biliar']
    col_usg=['Hallazgos ultrasonográficos']
    df_usg=pd.DataFrame(hallazgos_usg,usg_index,col_usg)
    df_usg.style.set_caption("Hello World")

    

    
    # ---------------------------------------------------------------------------- #
    #                                      ASA                                     #
    # ---------------------------------------------------------------------------- #
    #ASA
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    asaI=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE asa= 'I'  ''')
    asaI_count=cur.fetchone()
    
    asaII=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE asa= 'II'  ''')
    asaII_count=cur.fetchone()
    
    asaIII=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE asa= 'III'  ''')
    asaIII_count=cur.fetchone()
    
    asaIV=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE asa= 'IV'  ''')
    asaIV_count=cur.fetchone()
    
    asaV=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE asa= 'V'  ''')
    asaV_count=cur.fetchone()
    
    asadf=[asaI_count,asaII_count,asaIII_count,asaIV_count,asaV_count]
    asa_index=['ASA I', 'ASA II','ASA III','ASA IV','ASA V']
    column_asa=['Riesgo ASA']
    df_asa=pd.DataFrame(asadf,asa_index,column_asa)
   
    
    

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

    
    #Laboratorios prequirúrgicos
    Leu_count=cur.execute('''SELECT Leuing FROM Basecxcol ''')
    leu_ing=cur.fetchall()
    
    
  
   
    
    
    # ---------------------------------------------------------------------------- #
    #                              Inicio de síntomas                              #
    # ---------------------------------------------------------------------------- #
    #Tiempo de inicio de síntomas hasta cirugía
    tiempo_qxcount=cur.execute('''SELECT COUNT(Tiempoinsintqx) FROM Basecxcol ORDER BY DiasUCIposqx ASC  ''')
    tiempo_sintqx=tiempo_qxcount.fetchall()
    

    df_tiempo=(tiempo_sintqx)
    coluna=['Tiempo de inicio de síntomas']
    serie_tiempoqx=pd.DataFrame(tiempo_sintqx)
    st.dataframe(serie_tiempoqx)


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
    
    
    
    # ---------------------------------------------------------------------------- #
    #                              Duración de cirugía                             #
    # ---------------------------------------------------------------------------- #
    duracion_cx=cur.execute("""SELECT Duracionqx FROM Basecxcol WHERE Duracionqx !=1  """ )
    duracioncx=duracion_cx.fetchall()
    col_duracioncx=['Tiempo en minutos']
    #promedio_tiempo=cur.execute("""SELECT avg(Duracionqx) FROM Basecxcol""")
    #promediocx,=promedio_tiempo.fetchone()
    #df_duracioncx=[duracioncx]

    df_duracion=pd.DataFrame(duracioncx,columns=col_duracioncx)
   # ---------------------------------------------------------------------------- #
   #                             Conversión de cirugía                            #
   # ---------------------------------------------------------------------------- #
    #Conversión de cirugúa
    #conversion_si=cur.execute('SELECT FROM Basecxcol WHERE Conversión=1')
    #conversion_si_count=cur.fetchone()
    
    #Conversión_no=cur.execute('SELECT FROM Basecxcol WHERE Conversión=0')
    #consersionno_count=cur.fetchone()
    
    
    #Días de estancia 

    #Uso de vasopresor postquirúrgico

    # ---------------------------------------------------------------------------- #
    #                             Complicaciones postqx                            #
    # ---------------------------------------------------------------------------- #
    #Complicaciones postquirúrgicas
    con=sqlite3.connect('DB.db')
    cur=con.cursor()
    clavienI_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol  WHERE Comppostqx='I'AND Peso!=1 ''')
    clavienI=cur.fetchone()
    
    clavienII_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol  WHERE Comppostqx='II' AND Peso!=1 ''')
    clavienII=cur.fetchone()
    
    clavienIII_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol  WHERE Comppostqx='III' AND Peso!=1 ''')
    clavienIII=cur.fetchone()
    
    clavienIV_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol  WHERE Comppostqx='IV' AND Peso!=1 ''')
    clavienIV=cur.fetchone()
    
    clavienV_count=cur.execute('''SELECT COUNT(*) FROM Basecxcol  WHERE Comppostqx='V' AND PEso!=1 ''')
    clavienV=cur.fetchone()
    
    complicaciones_df=[clavienI,clavienII,clavienIII,clavienIV,clavienV]
    index_clavien=['I','II','III','IV','V']
    df_clavien=pd.DataFrame(complicaciones_df,index_clavien)
  
#Ventilación mecánica postquirúrgica

#Dias uci postqx

#Recurrencia de síntomas

# ---------------------------------------------------------------------------- #
#                                  Mortalidad                                  #
# ---------------------------------------------------------------------------- #
#Mortalidad
    con = sqlite3.connect('DB.db')
    cur = con.cursor()
   
    mort_si=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Muerte = "Si" AND Peso !=1''')
    Mort_count,=mort_si.fetchone()
    
    mort_no=cur.execute('''SELECT COUNT(*) FROM Basecxcol WHERE Muerte= "No" AND Peso !=1 ''')
    Mort_countno,=mort_no.fetchone()
    n_mort=Mort_countno+Mort_count
    global df_mortalidad
    global df_supervivencia
    
    mort_litiásica=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Muerte= "Si" AND Tipoccla ="Litiasica"')
    mortlit_count,=cur.fetchone()
    
    mort_alit=cur.execute('SELECT COUNT(*) FROM Basecxcol WHERE Muerte= "Si" AND Tipoccla ="Alitiasica"')
    mortalit_count,=cur.fetchone()
    
    
    porcentaje_mortalidad=(Mort_count/(Mort_count+Mort_countno))*100
    Supervivencia_porcentaje=(Mort_countno/(Mort_count+Mort_countno))*100
    supervvsmort=(Supervivencia_porcentaje,porcentaje_mortalidad)
    mortalidad=(Mort_count,Mort_countno,Supervivencia_porcentaje,porcentaje_mortalidad,n_mort,mortlit_count,mortalit_count)
    index_mortalidad=('Defunciones','Pacientes vivos','% Supervivencia','% Mortalidad','N','Mortalidad de pacientes con litiasis vesicular','Mortalidad de pacientes alitisicos')
    index_supervivencia=('Supervivientes','Mortalidad')
    columnas_mortalidad=['Número de pacientes']
    df_mortalidad=pd.DataFrame(mortalidad)
    df_supervivencia=pd.DataFrame(mortalidad,index_mortalidad,columnas_mortalidad)
    
  
    #Con el styler puedes modificar el dataframe
    
    #dff_mort=pd.DataFrame({'Mortalidad':mortalidad,'Supervivencia':Supervivencia_porcentaje},index=['Numero','Bola','Sin','Cos'])
    #df_stile=dff_mort.style.set_properties(**{'background-White': 'black',
      #                     'color': 'Blue'})
    # se declara mark_bar para las barras y luego se codifican los ejes con la X y Y que correponden al label
    #del diccionario
    
    
    
        

    # se tiene que hacer el formato de dataframe en forma de diccionario
    

# ---------------------------------------------------------------------------- #
#                                    Tablas                                    #
# ---------------------------------------------------------------------------- #

  # ---------------------------------------------------------------------------- #
    #                                    Tabla 1                                   #
    # ---------------------------------------------------------------------------- #
    Tabla_1_data=[avg_edad_count,23],[1,1],[masc_count,2],[fem_count,2],[peso_avg,2],[talla_promedio,1],[IMC_avg,1],[1,1],[DMcount,1],[HAScount,1],[valvcount,1],[IAMcount,1],[ICCcount,1],[EVCcount],[EPOCcount]
    index_tabla1=['Edad','Género','Masculino','Femenino','Peso','Talla','IMC','Comorbilidades','Diabetes mellitus','Hipertensión arterial','Valvulopatía','Infarto agudo al miocardio','Insuficiencia cardiáca','EVC','EPOC']
    column_tabla_1=['Promedio','Números prueba']
    tabla_1=pd.DataFrame(Tabla_1_data,index_tabla1,column_tabla_1)
    st.info('Tabla 1. Características base')
    st.dataframe(tabla_1)

    #Poner comobrilidades desglosadas
    #modificar dataframe para que se vean los títulos y modificar los subtítulos
    #Enviar datos a excel
    excel='prueba.xlsx'
    tabla_1.to_excel(excel)


    # ---------------------------------------------------------------------------- #
    #                                Clínica de ccla                               #
    # ---------------------------------------------------------------------------- #
    
    #Síntomas de ccla
    #Hallazgos USG
    #Hallazgos TAC
    # ---------------------------------------------------------------------------- #
    #                          Condiciones prequirúrgicas                          #
    # ---------------------------------------------------------------------------- #
    #Ventilación mecánica prequirúrgica
    #vasopresores prequirúrgicos
    #Tipo de vasopresor
    #Procedimiento desencadente
    #Dias UCI
    #ASA
    #Tokyo
    
    #Mortalidad y morbilidad con labs
    #Indicacodres bioquimicos
    
    #Mortalidad y morbilidad
    #Litiasis vs alitiasis
    
    #Mmorbilidad y mortalidad
    #Condiciones quirúrgicas
    #Tiempo de sintomas a cx
    #Tipo de cirugía
    #Duración de cirugía
    #Conversión de cirugía
    #hallazgos cirugía
    #Litiasis vs alitiasis
    #Complicaciones postquirúrgicas
    
 
 
 
 
    # ---------------------------------------------------------------------------- #
    #                         Tabla mortalidad y morbilidad                        #
    # ---------------------------------------------------------------------------- #
    