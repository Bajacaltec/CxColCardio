#Inicio del programa

import numpy
from numpy.core.fromnumeric import ptp
import pandas
import matplotlib
from PIL.Image import TRANSPOSE
from sqlalchemy import false
import streamlit as st
from streamlit.widgets import NoValue
from sympy import O
import Scoreing

# ---------------------------------------------------------------------------- #
#                            Ficha de identificación                           #
# ---------------------------------------------------------------------------- #
st.title("CxColCardio")
#'''Se buscará paciente con ID unico el NSS con agregado para no repetir el registro
#por lo que debe ser completado'''
nss = st.text_input(
    "Registrar paciente con NSS colocar agregado sin espacios")
NSS = nss.upper()  # Hace el input de nss en mayuscular para que no falle el if con mayuscula
if NSS == "":
    st.image("CMN SXXI.jpeg", None, 600, 500)
    buscar = st.text_input("Busqueda de paciente")
elif NSS != "":
    st.sidebar.markdown("Registra los datos del nuevo paciente")
    st.sidebar.image("CMN SXXI.jpeg", None)
    col1, col2 = st.beta_columns(2)
    with col1:
        nom = st.text_input("Nombre del paciente")
    with col2:
        edad = st.number_input("Edad", 1, 120, 1)
    col1, col2, col3 = st.beta_columns(3)
    with col1:
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
        st.write("Bienvenida", " se esta completando el registro de ", nom)
    else:
        st.write("Bienvenido", " se esta completando el registro de", nom)
        Genero = "Masculino"

#Antecedentes del paciente
# ---------------------------------------------------------------------------- #
#                                 Antecedentes                                 #
# ---------------------------------------------------------------------------- #
 #Antecedentes
    st.subheader("Antecedentes")
    col1, col2 = st.beta_columns(2)
    with col1:
        comor = st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia",
                               "Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Otros"])
        tab=st.checkbox("Tabaquismo")
        if tab==True:
            st.number_input("Cajetillas/año",1,7000,1,1)
 with col2:
        Tipocxcardio = st.multiselect("Procedimientos cardiovasculares", [
                                      "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"])
  with col1:
        usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"])
    with col1:
        if usovasopr == "Si":
            tipovasopr = st.multiselect("Que vasopresor se utilizó", [
                                        "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
    col1, col2 = st.beta_columns(2)
    with col1:
        ventprol = st.number_input(
            "Días con ventilación mecánica", 0, 100, 0, 1)
        uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)
    with col2:
        compli = st.selectbox(
            "Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"])

# ---------------------------------------------------------------------------- #
#                            Laboratorios de ingreso                           #
# ---------------------------------------------------------------------------- #
#Laboratorios al ingreso
#Sección de laboratorios
sol1,sol2,sol3,sol4=st.beta_columns(4)
with sol1:
    ADE=st.number_input("ADE",0,100)
with sol2:
    PCR=st.number_input("PCR mg/dl"),0,700
with sol3:
    Leu=st.number_input("Leucocitos mm3",0,100000)
with sol4:
    AST=st.number_input("AST",0,1000)
with sol1:
    ALT=st.number_input("ALT",0,1000)
with sol2:
    Bil=st.number_input("Bilirrubinas totales",0,100)
with sol3:
    FA=st.number_input("FA",0)
with sol4:
    INR=st.number_input("INR",0)
with sol1:
    GGT=st.number_input("GGT",0)
with sol1:
    NA=st.number_input('Sodio')
with sol2:
    K=st.number_input('Potasio')
with sol3:
    pH=st.number_input("PH")
with sol4:
    Hto=st.number_input("Hematocrito")
with sol1:
    Creat=st.number_input("Creatinina")
with sol2:
    Leuc=st.number_input("Leucocitos")

    #Score de ingreso
# ---------------------------------------------------------------------------- #
#                               Score de ingreso                               #
# ---------------------------------------------------------------------------- #


#Sofa
Scoreing.SOFA()

Scoreing.apache()

# ---------------------------------------------------------------------------- #
#                                     CCLA                                     #
# ---------------------------------------------------------------------------- #
#CCLA
 col1, col2 = st.beta_columns(2)
    with col1:
        sysint = st.multiselect("Sintomas compatibles con colecistitis aguda", [
                                "Dolor en hipocondrio derecho", "Signo de Murphy", "Nausea y vómito","Ictericia","Fiebre","Dolor abdominal difuso","Estreñimiento"])
    with col2:
        usghall = st.multiselect("Hallazgos de ultrasonido", ["Engrosamiento de pared", "Líquido perivesicular", "Litiasis vesicular",
                                 "Distensión vesicular", "Gas intravesicular", "Lodo biliar", "Absceso perivesicular", "Anormalidad anatomíca"])
        taclla= st.multiselect("Hallagos Tomográficos",["Engrosamiento de la pared","Líquido perivesicular","Pérdida de la captación del contraste","Gas dentro de la vesícula biliar"])
    with col1:
           with col2:
        ASA = st.selectbox("ASA", ["I", "II", "III", "IV", "V", "VI"])
        asacheck = st.checkbox("ASA clasificación")
        if asacheck == True:
            st.image("ASA.png")
    col1, col2 = st.beta_columns(2)
    with col1:
        sevcole = st.selectbox("Severidad (Tokio 18)", [
                               "Leve", "Moderado", "Severo"])
        tokio = st.checkbox("Clasificación de Tokio 18")
        if tokio == True:
            st.image("Tokio.png")


# ---------------------------------------------------------------------------- #
#                       Laboratorios previos a la cirugía                      #
# ---------------------------------------------------------------------------- #
#Sección de laboratorios

st.subheader("Laboratorios previos a la cirugía")

tol1,tol2,tol3,tol4=st.beta_columns(4)
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

# ---------------------------------------------------------------------------- #
#                          Scores previos a la cirugía                         #
# ---------------------------------------------------------------------------- #

#Importar los módulos de SOFA y APACHEII


####
# ---------------------------------------------------------------------------- #
#                              Datos de la cirugía                             #
# ---------------------------------------------------------------------------- #

st.subheader("Datos de la cirugía")
col1,col2=st.beta_columns(2)
with col1:
    tiempevolcx=st.number_input("Tiempo desde el inicio de los síntomas al tratamiento quirúrgico",0,600,0,1)
    duracioncx=st.number_input("Duración de la cirugía (minutos)",1,700000,NoValue(),1)
    recurrencia=st.checkbox("Recurrencia de lo síntomas")
with col2:
    tipocx=st.selectbox("Tipo de cirugía (abierta o laparoscopica)",["Laparoscopica","Abierta"])
    convcx=st.checkbox("Conversión de cirugía laparoscopica a abierta")
    timeppostqx=st.number_input("Días de estancia posterior a tratamiento quirúrgico de colecistitis",1,60000,1,1)

# ---------------------------------------------------------------------------- #
#                           Evolución postquirúrgica                           #
# ---------------------------------------------------------------------------- #
#Evolucion postquirúrgica
  with col1:
        usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"])
    with col1:
        if usovasopr == "Si":
            tipovasopr = st.multiselect("Que vasopresor se utilizó", [
                                        "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
    col1, col2 = st.beta_columns(2)
    with col1:
        ventprol = st.number_input(
            "Días con ventilación mecánica", 0, 100, 0, 1)
        uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)
    with col2:
        compli = st.selectbox(
            "Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"])
recur=st.selectbox('Recurrencia de los síntomas',['No','Si'])
mort=st.selectbox("Muerte en los primeros 30 días posquirúrgicos",["No","Si"])
