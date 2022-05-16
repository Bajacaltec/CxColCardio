from distutils.log import error
from locale import ALT_DIGITS
from sqlalchemy import true
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3

from sympy import PythonIntegerRing
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
from itertools import chain
from Paginas.apache import PAM, creatdef, cronicos, cronicospreqx, edas, fcdef, htodef, kdef, leut, nadef, oxigen,frdef, phdef

from Paginas.apache import tempdef
      
def ficha_id():
    with st.expander('Identificación y somatometría',True):
        con = sqlite3.connect('Basededatos.db')
        cur = con.cursor()
        col1,col2=st.columns(2)
        
        sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
        nom=cur.fetchall()
        res = []
        for i in chain(*nom):
            res.append(i)
          
        with col1:
            global nambre
            nombre=(st.selectbox('Nombre',res), )
            nambre=str(nombre)
        con.commit()
        con.close()
        con = sqlite3.connect('Basededatos.db')
        cur = con.cursor()
        
        recabar=cur.execute("SELECT * FROM cxcolcardio WHERE Nombre=(?)",(nombre))
        bas,=cur.fetchall()
        with col2:
            global NSS
            NSS=st.text_input("NSS",bas[2])
        with col1:
            global edad
            edad=st.number_input('Edad',1,200,bas[1])
        col1,col2,col3=st.columns(3)
        with col1:
            global peso
            peso = st.number_input("Peso", 1, None, 1, 1)
        with col2:
            global talla
            talla = st.number_input("Talla", 0.1, None, 1.0, 0.1)
        with col3:
            global imc
            imc = peso/talla**2
            indiceMC = st.number_input("IMC",None,None,imc,0.1,disabled=True)
            global Genero
        Genero = "F" in NSS
        if Genero == True:
            #Para modificar el markdown con HTML se usa ese codigo de abajo
            #willkomen = '<p style="font-family:Times; color:Brown; font-size: 60px;">Bienvenida</p>'
            #st.markdown(willkomen, unsafe_allow_html=True)
            Genero = "Femenino"
        else:
            Genero = "Masculino"
            
def antecedentes():
    with st.expander('Antecedentes'):
        col1,col2,col3=st.columns(3)
        with col1:
            global comor
            comor = str(st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia",
                                    "Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Otros"]))
        with col2:
            global tab
            tab=str(st.selectbox("Tabaquismo",['No','Si']))
            if tab=='Si':
                global cajetillas
                cajetillas=st.number_input("Cajetillas/año",1,7000,1,1)
            else:
                cajetillas='NA'
            global cronicosapache
        with col3:
            cronicosapache=str(st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos']))
        with col1:
            global Tipocxcardio
            Tipocxcardio =str(st.multiselect("Procedimientos cardiovasculares", [
                                            "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"]))
        with col2:
            global usovasopr
            usovasopr = str(st.selectbox("Uso de vasopresores previos a cirugía por CCLA", ["No", "Si"]))
            if usovasopr == "Si":
                global tipovasopr
                tipovasopr = str(st.multiselect("Que vasopresor se utilizó", ["Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"]))
            else:
                tipovasopr='NA'
        with col3:
            global ventprol
            ventprol = st.number_input(
                    "Días con ventilación mecánica previo a cirugía", 0, 100, 0, 1)
        with col1:
            global uciestpreop
            uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)
        

def vitales_ingreso():
     with st.expander('Signos vitales'):
        vol1,vol2,vol3,vol4=st.columns(4)
        with vol1:
            global FC
            FC=st.number_input("FC/min",1,300,80,1)
        with vol2:
            global FR
            FR=st.number_input("Fr/min",1,300,20,1)
        with vol3:
            global Sisting
            Sisting=st.number_input('Sistólica',1,300,110,1)
        with vol4:
            global Diasting
            Diasting=st.number_input('Diastólica',1,300,80,1)
        with vol1:
            global Temping
            Temping=st.number_input('T°C',34.1,45.1,37.1,0.1)
        with vol2:
            global uresising
            uresising=st.number_input("Uresis/dia",1,100000,1,1)
        with vol3:
            global tiempocuant
            tiempocuant=st.number_input('Horas de la cuantificación',1,24,24)
            global ukghr
            ukghr=float((uresising/peso)/tiempocuant)


def labs_ingreso():
    #Laboratorios al ingreso
    #Sección de laboratorios
    with st.expander('Laboratorios de ingreso'):
        sol1,sol2,sol3,sol4=st.columns(4)
        with sol1:
            global ADE
            ADE=st.number_input("ADE",0,1000,key='<ADE preqx>')
        with sol2:
            global PCR
            PCR=st.number_input("PCR mg/dl",key='<pcr>')
        with sol3:
            global AST
            AST=st.number_input("AST",0,100000,key='<ast>')
        with sol4:
            global ALT
            ALT=st.number_input("ALT ",0,100000)
        with sol1:
            global Bil
            Bil=st.number_input("Bil tot ",0.1,100.1,1.0,0.1)
        with sol2:
            global FA
            FA=st.number_input("FA ",0)
        with sol3:
            global INR
            INR=st.number_input("INR ",0.1,100.1,1.0,0.1)
        with sol4:
            global GGT
            GGT=st.number_input("GGT ",0)
        with sol1:
            global NA
            NA=st.number_input('Sodio',1,200,140)
        with sol2:
            global K
            K=st.number_input('Potasio ')
        
        with sol4:
            global Hto
            Hto=st.number_input("Hematocrito ",1,100)
        with sol3:
            global creating
            creating=st.number_input("Creatinina ")
        with sol2:
            global Leuc
            Leuc=st.number_input("Leucocitos ",1,1000000000)
        with sol4:
            global plaqing
            plaqing=st.number_input("Plaquetas",1)
        with sol1:
            global pHing
            pHing=st.number_input('pH en gasometría de ingreso')

def SOFA():
    with st.expander('SOFA/Ingreso'):
        col1, col2, col3 = st.columns(3)
        with col1:
            global PaO2
            PaO2 = st.number_input("PaO2 en mmHg", 1, None, 1)
            global Aado2
            Aado2=st.number_input("AaDO2",1,None,1)
        with col2:
            global FiO2
            FiO2 = st.number_input("FiO2 %", 1, None)
        with col3:
            global ventmec
            ventmec = str(st.selectbox("¿Ventilación mecánica?", ["No", "Si"]))
        Resp(PaO2,FiO2,ventmec)

        with col2:
            global Glasgow
            Glasgow = st.number_input("Escala de coma de Glasgow", 1, 15, 15, 1)
        Neu(Glasgow)
        metabol(Bil)
        global vasopres
        vasopres=str(st.selectbox("Uso de vasopresores",["Sin vasopresor","Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis","Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min","Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min"]))
        cardio(Diasting,Sisting,vasopres)
        coag(plaqing)
        urin(creating,uresising)
        global Sofapt
        Sofapt=(Resp.PtResp+Neu.Ptneu+metabol.biling+cardio.carding+coag.sofplaqing+urin.sofcreating)            
            
       #Termina SOFA
def apache(): 
    tempdef(Temping)
    PAM(Diasting,Sisting)
    fcdef(FC)
    frdef(FR)
    oxigen(FiO2,Aado2,PaO2)
    phdef(pHing)
    nadef(NA)
    kdef(K)
    creatdef(creating)
    htodef(Hto)
    leut(Leuc)
    edas(edad)
    cronicos(cronicosapache)
    global apacheing
    apacheing=tempdef.pttemp+PAM.ptpam+fcdef.fcpt+frdef.frpt+phdef.phpt+nadef.napt+kdef.kpt+creatdef.creatpt+htodef.htopt+leut.leupt+edas.edadpt+cronicos.ptestado+oxigen.opt
    st.write(apacheing)
            
def sintomas_ccla():
     with st.expander('Síntomas de CCLA'):
        col1, col2 = st.columns(2)
        with col1:
            global sysint
            sysint = str(st.multiselect('Sintomas compatibles',["Dolor en hipocondrio derecho", "Signo de Murphy", "Nausea y vómito","Ictericia","Fiebre","Dolor abdominal difuso","Estreñimiento"]))
        with col2:
            global usghall
            usghall = str(st.multiselect("Hallazgos de ultrasonido", ["Engrosamiento de pared", "Líquido perivesicular", "Litiasis vesicular",
                                        "Distensión vesicular", "Gas intravesicular", "Lodo biliar", "Absceso perivesicular", "Anormalidad anatomíca"]))
            global tachall
            tachall= str(st.multiselect("Hallazgos tomográficos",["Engrosamiento de la pared","Líquido perivesicular","Pérdida de la captación del contraste","Gas dentro de la vesícula biliar"]))
        with col1:
            global asa
            asa=str(st.selectbox("ASA", ["I", "II", "III", "IV", "V", "VI"]))
            asacheck = st.checkbox("ASA clasificación")
            if asacheck == True:
                st.image("/Users/alonso/CxColCardio/Paginas/Imagenes/ASA.png")
        col1, col2 = st.columns(2)
        with col1:
            global sevcole
            sevcole = str(st.selectbox("Severidad (Tokio 18)", [
                                    "Leve", "Moderado", "Severo"]))
            tokio = st.checkbox("Clasificación de Tokio 18")
            if tokio == True:
                st.image("/Users/alonso/CxColCardio/Paginas/Imagenes/Tokio.png")
                
def labs_preqx():
    with st.expander('Laboratorios previos a la cirugía'):

        tol1,tol2,tol3,tol4=st.columns(4)
        with tol1:
            global ADEcx
            ADEcx=st.number_input("ADE",0,100)
        with tol2:
            global PCRcx
            PCRcx=st.number_input(("PCR mg/dl"),0.1,700.0,1.0,0.1)
        with tol3:
            global Leucx
            Leucx=st.number_input("Leucocitos mm3",0,100000)
        with tol4:
            global ASTcx
            ASTcx=st.number_input("AST",0)
        with tol1:
            global ALTcx
            ALTcx=st.number_input("ALT",0)
        with tol2:
            global Bilcx
            Bilcx=st.number_input("Bilirrubinas totales")
        with tol3:
            global FAcx
            FAcx=st.number_input("FA",0)
        with tol4:
            global INRcx
            INRcx=st.number_input("INR")
        with tol1:
            global GGTcx
            GGTcx=st.number_input("GGT",0)
        with tol2:
            global NAcx
            NAcx=st.number_input('Sodio',0)
        with tol3:
            global Kcx
            Kcx=st.number_input('Potasio')
        with tol4:
            global pHcx
            pHcx=st.number_input("PH")
        with tol1:
            global Htocx
            Htocx=st.number_input("Hematocrito",0)
        with tol2:
            global Creatcx
            Creatcx=st.number_input("Creatinina")
        with tol3:
            global Leuccx
            Leuccx=st.number_input("Leucocitos",0)
        with tol4:
            global plaqqx
            plaqqx=st.number_input("Plaquetaspreqx",0)
        with tol1:
            global pHpreqx
            pHpreqx=st.number_input('pH en gasometría prequirúrgica')
            
def datos_cirugia():
     with st.expander("Datos de la cirugía"):
        col1,col2=st.columns(2)
        with col1:
            global tiempevolcx
            tiempevolcx=st.number_input("Tiempo desde el inicio de los síntomas al tratamiento quirúrgico",0,600,0,1)
            global duracioncx
            duracioncx=st.number_input("Duración de la cirugía (minutos)",1,700000,1,1)
            recurrencia=st.checkbox("Recurrencia de lo síntomas")
        with col2:
            global tipocx
            tipocx=str(st.selectbox("Tipo de cirugía (abierta o laparoscopica)",["Laparoscopica","Abierta"]))
            global convcx
            convcx=st.checkbox("Conversión de cirugía laparoscopica a abierta")
            global timeppostqx
            timeppostqx=st.number_input("Días de estancia posterior a tratamiento quirúrgico de colecistitis",1,60000,1,1)
            
def datos_postcirugia():
    with st.expander('Evolución postquirúrgica'):
        col1, col2, col3 = st.columns(3)
        with col1:
            global usovasopr
            usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"],key='>Postqxvasopres')
            if usovasopr == "Si":
                tipovasopr = st.multiselect("Que vasopresor se utilizó postqx", [
                                            "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
        with col2:
            global ventprol
            ventprol = st.number_input("Días con ventilación mecánica", 0, 100, 0, 1,key='<Postqxventilación>')
        with col3:
            global uciestpreop
            uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1,key='<uci>')
        with col1:
            global compli
            compli = st.selectbox("Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"],key='<estamera>')
        with col2:
            global recur    
            recur=st.selectbox('Recurrencia de los síntomas',['No','Si'])
        with col3:
            global mort
            mort=st.selectbox("Muerte en los primeros 30 días posquirúrgicos",["No","Si"])

def registrarcapturaenbase():
        regis=st.button("Registrar")
        prueba=10
        if regis==True:
            con = sqlite3.connect('DB.db')
            cur = con.cursor()
            cur.execute("""INSERT INTO Basefinal(SOFApreqx,Apachepreqx,Apacheing,PCRpreqx,Leupreqx,ADEpreqx,Tokyo,Hallazgtom,asa,Nombre,Edad,NSS,Peso,Talla,IMC,Crónicos,Tabaquismo,Cajetillas,Diasventmec,Crónicosapache,Vasopresores,Tipovasopresor,PRoccardio,DiasUCIpreqx,FCing,FRing,Sising,Diasing,Temping,Uresising,Horasing,ADEing,PCRing,ASTing,ALTing,Biltoting,FAing,INRing,GGTing,King,PHing,Hematocritoing,Naing,Leuing,Creating,Plaquetasing,PAO2ing,FIO2ing,Ventilacionmec,AaDO2ing,Glasgowing,SOFAing,Vasopresor,Sintomascompatccla,Hallazusg,Leupreqx,ASTpreqx,ALTpreqx,Biltotpreqx,FApreqx,INRpreqx,GGTpreqx,Kpreqx,PHpreqx,HTOpreqx,NApreqx,Creatpreqx,Tiempoinsintqx,tipoqx,Duracionqx,Conversión,Diasestancia,postqxvasopresor,Comppostqx,Ventmecpostqx,DiasUCIposqx,Recurrsint,Muerte)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (Sofaptpreqx,apachepreqx,apacheing,PCRcx,Leucx,ADEcx,sevcole,tachall,asa,nambre,edad,NSS,peso,talla,imc,comor,tab,cajetillas,ventprol,cronicosapache,usovasopr,tipovasopr,Tipocxcardio,uciestpreop,FC,FR,Sisting,Diasting,Temping,uresising,tiempocuant,ADE,PCR,AST,ALT,Bil,FA,INR,GGT,K,pHing,Hto,NA,Leuc,creating,plaqing,PaO2,FiO2,ventmec,Aado2,Glasgow,Sofapt,vasopres,sysint,usghall,Leucx,ASTcx,ALTcx,Bilcx,FAcx,INRcx,GGTcx,Kcx,pHcx,Htocx,NAcx,Creatcx,tiempevolcx,tipocx,duracioncx,convcx,timeppostqx,usovasopr,compli,ventprol,uciestpreop,recur,mort))
            con.commit()
            con.close()         
            st.success('Registro existoso')
            st.balloons()


def vitales_preqx():
     with st.expander('Signos vitales prequirúrgicos'):
        vol1,vol2,vol3,vol4=st.columns(4)
        with vol1:
            global FCqx
            FCqx=st.number_input("FCpreqx/min",1,300,80,1)
        with vol2:
            global FRqx
            FRqx=st.number_input("Frpreqx/min",1,300,20,1)
        with vol3:
            global Sistingqx
            Sistingqx=st.number_input('Sistólicapreqx',1,300,110,1)
        with vol4:
            global Diastqx
            Diastqx=st.number_input('Diastólicapreqx',1,300,80,1)
        with vol1:
            global Tempqx
            Tempqx=st.number_input('T°Cpreqx',34.1,45.1,37.1,0.1)
        with vol2:
            global uresisqx
            uresisqx=st.number_input("Uresis/diapreqx",1,100000,1,1)
        with vol3:
            global tiempocuantqx
            tiempocuantqx=st.number_input('Horas de la cuantificación preqx',1,24,24)
            global ukghr
            ukghrqx=float((uresising/peso)/tiempocuant)
def SOFApreqx():
    with st.expander('SOFA/preqx'):
        col1, col2, col3 = st.columns(3)
        with col1:
            global PaO2preqx
            PaO2preqx = st.number_input("PaO2preqx en mmHg", 1, None, 1)
            global Aado2preqx
            Aado2preqx=st.number_input("AaDO2preqx",1,None,1)
        with col2:
            global FiO2preqx
            FiO2preqx = st.number_input("FiO2preqx %", 1, None)
        with col3:
            global ventmecpreqx
            ventmecpreqx = str(st.selectbox("¿Ventilación mecánicapreqx?", ["No", "Si"]))
        Resp(PaO2preqx,FiO2preqx,ventmecpreqx)

        with col2:
            global Glasgowpreqx
            Glasgowpreqx = st.number_input("Escala de coma de Glasgowpreqx", 1, 15, 1, 1)
        Neu(Glasgowpreqx)
        metabol(Bilcx)
        global vasoprespreqx
        vasoprespreqx=str(st.selectbox("Uso de vasopresorespreqx",["Sin vasopresor","Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis","Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min","Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min"]))
        cardio(Diastqx,Sistingqx,vasoprespreqx)
        coag(plaqqx)
        urin(Creatcx,uresisqx)
        global Sofaptpreqx
        Sofaptpreqx=(Resp.PtResp+Neu.Ptneu+metabol.biling+cardio.carding+coag.sofplaqing+urin.sofcreating)            
        st.write(Sofaptpreqx)
def apachepreqx1(): 
    tempdef(Tempqx)
    PAM(Diastqx,Sistingqx)
    fcdef(FCqx)
    frdef(FRqx)
    oxigen(FiO2preqx,Aado2preqx,PaO2preqx)
    phdef(pHpreqx)
    nadef(NAcx)
    kdef(Kcx)
    creatdef(Creatcx)
    htodef(Htocx)
    leut(Leuccx)
    edas(edad)
    with st.expander('APACHE IIpreqx'):
            global estadopreqx
            estadopreqx=st.selectbox("Estadopreqx",['No quirúrgico','Programado','Urgencia'])
    cronicospreqx(estadopreqx)
    global apachepreqx
    apachepreqx=tempdef.pttemp+PAM.ptpam+fcdef.fcpt+frdef.frpt+oxigen.opt+phdef.phpt+nadef.napt+kdef.kpt+creatdef.creatpt+htodef.htopt+leut.leupt+edas.edadpt+cronicos.ptestado
    st.write(apachepreqx)