import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin

def ficha_id():
    with st.expander('Identificación y somatometría'):
        con = sqlite3.connect('Basededatos.db')
        cur = con.cursor()
        sumedad=cur.execute('''Select Nombre FROM cxcolcardio''')
        nom=cur.fetchall()
        
        nombre=st.selectbox('Nombre',nom) 
        nssbase=cur.execute('''Select Nss FROM cxcolcardio WHERE Nombre=(?)''',nombre)
        guu,=(cur.fetchone())
        NSS=st.text_input("NSS",guu)
        edad=st.number_input('Edad',1,120,1,1)
        col1,col2,col3=st.columns(3)
        st.subheader('Captura de datos')
        st.title("CxColCardio")
        with col1:
            global peso
            peso = st.number_input("Peso", 1, None, 1, 1)
        with col2:
            talla = st.number_input("Talla", 0.1, None, 1.0, 0.1)
        with col3:
            imc = peso/talla**2
            indiceMC = st.number_input("IMC", 1.0, None, imc, 0.1)
        Genero = "F" in NSS
        if Genero == True:
            #Para modificar el markdown con HTML se usa ese codigo de abajo
            #willkomen = '<p style="font-family:Times; color:Brown; font-size: 60px;">Bienvenida</p>'
            #st.markdown(willkomen, unsafe_allow_html=True)
            Genero = "Femenino"
            st.write("Bienvenida", " se esta completando el registro de ", nombre)
        else:
            st.write("Bienvenido", " se esta completando el registro de", nombre)
            Genero = "Masculino"
            
def antecedentes():
    with st.expander('Antecedentes'):
        st.subheader("Antecedentes")
        col1,col2,col3=st.columns(3)
        with col3:
            comor = st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia",
                                    "Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Otros"])
            tab=st.checkbox("Tabaquismo")
            if tab==True:
                st.number_input("Cajetillas/año",1,7000,1,1)
            cronicosapache=st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos'])
        with col1:
            Tipocxcardio = st.multiselect("Procedimientos cardiovasculares", [
                                            "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"])
        with col2:
            usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"])
            if usovasopr == "Si":
                tipovasopr = st.multiselect("Que vasopresor se utilizó", [
                                                "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
        with col3:
            ventprol = st.number_input(
                    "Días con ventilación mecánica", 0, 100, 0, 1)
            uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)
        with col1:
            compli = st.selectbox(
                    "Complicaciones postoperatorias (Clavien-Dindo)", ["I", "II", "III", "IV", "V"])

def vitales_ingreso():
     with st.expander('Signos vitales'):
        st.subheader("Signos vitales de ingreso")
        vol1,vol2,vol3,vol4=st.columns(4)
        with vol1:
            FC=st.number_input("FC/min",1,300,80,1)
        with vol2:
            FR=st.number_input("Fr/min",1,300,20,1)
        with vol3:
            global Sisting
            Sisting=st.number_input('Sistólica',1,300,110,1)
        with vol4:
            global Diasting
            Diasting=st.number_input('Diastólica',1,300,80,1)
        with vol1:
            Temping=st.number_input('T°C',34.1,45.1,37.1,0.1)
        with vol2:
            global uresising
            uresising=st.number_input("Uresis/dia",1,100000,1,1)
        with vol3:
            tiempocuant=st.number_input('Horas de la cuantificación',1,24,24)
            ukghr=float((uresising/peso)/tiempocuant)
        st.subheader('Uresis por kg por hora')
        st.warning(ukghr)


def labs_ingreso():
    #Laboratorios al ingreso
    #Sección de laboratorios
    with st.expander('Laboratorios de ingreso'):
        st.subheader('Laboratorios de ingreso')
        sol1,sol2,sol3,sol4=st.columns(4)
        with sol1:
            ADE=st.number_input("ADE",0,100,key='<ADE preqx>')
        with sol2:
            PCR=st.number_input("PCR mg/dl",key='<pcr>')
        with sol3:
            Leu=st.number_input("Leucocitos  mm3",0,100000)
        with sol4:
            AST=st.number_input("AST",0,1000,key='<ast>')
        with sol1:
            ALT=st.number_input("ALT ",0,1000)
        with sol2:
            global Bil
            Bil=st.number_input("Bil tot ",0,100)
        with sol3:
            FA=st.number_input("FA ",0)
        with sol4:
            INR=st.number_input("INR ",0)
        with sol1:
            GGT=st.number_input("GGT ",0)
        with sol1:
            NA=st.number_input('Sodio',1,200,140)
        with sol2:
            K=st.number_input('Potasio ')
        with sol3:
            pH=st.number_input("PH ")
        with sol4:
            Hto=st.number_input("Hematocrito ")
        with sol3:
            global creating
            creating=st.number_input("Creatinina ")
        with sol2:
            Leuc=st.number_input("Leucocitos ")
        with sol4:
            global plaqing
            plaqing=st.number_input("Plaquetas")

def SOFA():
    with st.expander('SOFA de ingreso'):
        st.subheader("SOFA de ingreso")
        col1, col2, col3 = st.columns(3)
        with col1:
            PaO2 = st.number_input("PaO2 en mmHg", 1, None, 1)
            Aado2=st.number_input("AaDO2",1,None,1)
        with col2:
            FiO2 = st.number_input("FiO2 %", 1, None)
        with col3:
            ventmec = st.selectbox("¿Ventilación mecánica?", ["No", "Si"])
        Resp(PaO2,FiO2,ventmec)

        with col1:
            Glasgow = st.number_input("Escala de coma de Glasgow", 1, 15, 1, 1)
        Neu(Glasgow)
        metabol(Bil)
        cardio(Diasting,Sisting)
        coag(plaqing)
        urin(creating,uresising)
        calcular_sofa=st.checkbox('Calcular SOFA')
        if calcular_sofa==True:
            Sofapt=(Resp.PtResp+Neu.Ptneu+metabol.biling+cardio.carding+coag.sofplaqing+urin.sofcreating)            
            st.subheader("SOFA score")
            st.info(Sofapt)
        #Termina SOFA
        
def sintomas_ccla():
     with st.expander('síntomas de CCLA'):
        st.subheader("CCLA")
        col1, col2 = st.columns(2)
        with col1:
            sysint = st.multiselect("Sintomas compatibles con colecistitis aguda", [
                                    "Dolor en hipocondrio derecho", "Signo de Murphy", "Nausea y vómito","Ictericia","Fiebre","Dolor abdominal difuso","Estreñimiento"])
        with col2:
            usghall = st.multiselect("Hallazgos de ultrasonido", ["Engrosamiento de pared", "Líquido perivesicular", "Litiasis vesicular",
                                        "Distensión vesicular", "Gas intravesicular", "Lodo biliar", "Absceso perivesicular", "Anormalidad anatomíca"])
            taclla= st.multiselect("Hallagos Tomográficos",["Engrosamiento de la pared","Líquido perivesicular","Pérdida de la captación del contraste","Gas dentro de la vesícula biliar"])
        with col1:
            ASA=st.selectbox("ASA", ["I", "II", "III", "IV", "V", "VI"])
            asacheck = st.checkbox("ASA clasificación")
            if asacheck == True:
                st.image("ASA.png")
        col1, col2 = st.columns(2)
        with col1:
            sevcole = st.selectbox("Severidad (Tokio 18)", [
                                    "Leve", "Moderado", "Severo"])
            tokio = st.checkbox("Clasificación de Tokio 18")
            if tokio == True:
                st.image("Tokio.png")
                
def labs_preqx():
    with st.expander('Laboratorios previos a la cirugía'):
        st.subheader("Laboratorios previos a la cirugía")

        tol1,tol2,tol3,tol4=st.columns(4)
        with tol1:
            ADEcx=st.number_input("ADE",0,100)
        with tol2:
            PCRcx=st.number_input("PCR mg/dl"),0,700
        with tol3:
            Leucx=st.number_input("Leucocitos mm3",0,100000)
        with tol4:
            ASTcx=st.number_input("AST",0,1000)
        with tol1:
            ALTcx=st.number_input("ALT",0,1000)
        with tol2:
            Bilcx=st.number_input("Bilirrubinas totales",0,100)
        with tol3:
            FAcx=st.number_input("FA",0)
        with tol4:
            INRcx=st.number_input("INR",0)
        with tol1:
            GGTcx=st.number_input("GGT",0)
        with tol1:
            NAcx=st.number_input('Sodio')
        with tol2:
            Kcx=st.number_input('Potasio')
        with tol3:
            pHcx=st.number_input("PH")
        with tol4:
            Htocx=st.number_input("Hematocrito")
        with tol1:
            Creatcx=st.number_input("Creatinina")
        with tol2:
            Leuccx=st.number_input("Leucocitos")
            
def datos_cirugia():
     with st.expander("Datos de la cirugía"):
        st.subheader("Datos de la cirugía")
        col1,col2=st.columns(2)
        with col1:
            tiempevolcx=st.number_input("Tiempo desde el inicio de los síntomas al tratamiento quirúrgico",0,600,0,1)
            duracioncx=st.number_input("Duración de la cirugía (minutos)",1,700000,1,1)
            recurrencia=st.checkbox("Recurrencia de lo síntomas")
        with col2:
            tipocx=st.selectbox("Tipo de cirugía (abierta o laparoscopica)",["Laparoscopica","Abierta"])
            convcx=st.checkbox("Conversión de cirugía laparoscopica a abierta")
            timeppostqx=st.number_input("Días de estancia posterior a tratamiento quirúrgico de colecistitis",1,60000,1,1)
            
def datos_postcirugia():
    with st.expander('Evolución postquirúrgica'):
        col1, col2 = st.columns(2)
        with col1:
            usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"],key='>Postqxvasopres')
        with col1:
            if usovasopr == "Si":
                tipovasopr = st.multiselect("Que vasopresor se utilizó", [
                                            "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
        with col1:
            ventprol = st.number_input("Días con ventilación mecánica", 0, 100, 0, 1,key='<Postqxventilación>')
            uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1,key='<uci>')
        with col2:
            compli = st.selectbox("Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"],key='<estamera>')
        recur=st.selectbox('Recurrencia de los síntomas',['No','Si'])
        mort=st.selectbox("Muerte en los primeros 30 días posquirúrgicos",["No","Si"])

def registrarcapturaenbase():
        regis=st.button("Registrar")
        if regis==True:
            st.success('Registro existoso')
            st.balloons()