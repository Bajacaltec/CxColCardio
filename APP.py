#Tesis de cirugía en pacientes con colecistitis alitiásica
import numpy
from numpy.core.fromnumeric import ptp
import pandas
import matplotlib
from PIL.Image import TRANSPOSE
from sqlalchemy import false
import streamlit as st
from streamlit.widgets import NoValue
from sympy import O
st.title("CxColCardio")
#'''Se buscará paciente con ID unico el NSS con agregado para no repetir el registro
#por lo que debe ser completado'''
nss = st.sidebar.text_input(
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
    #Antecedentes
    st.subheader("Antecedentes")
    col1, col2 = st.beta_columns(2)
    with col1:
        comor = st.multiselect("Enfermedades crónicas", ["Diabetes mellitus", "Hipertensión arterial", "Valvulopatia",
                               "Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Otros"])
    with col2:
        usghall = st.multiselect("Hallazgos de ultrasonido", ["Engrosamiento de pared", "Líquido perivesicular", "Litiasis vesicular",
                                 "Distensión vesicular", "Gas intravesicular", "Lodo biliar", "Absceso perivesicular", "Anormalidad anatomíca"])
    col1, col2 = st.beta_columns(2)
    with col1:
        usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"])
    with col2:
        if usovasopr == "Si":
            tipovasopr = st.multiselect("Que vasopresor se utilizó", [
                                        "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
    col1, col2 = st.beta_columns(2)
    with col1:
        ventprol = st.number_input(
            "Días con ventilación mecánica", 0, 100, 0, 1)
    with col2:
        compli = st.selectbox(
            "Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"])
    col1, col2 = st.beta_columns(2)
    with col1:
        sysint = st.multiselect("Sintomas compatibles con colecistitis aguda", [
                                "Dolor en hipocondrio derecho", "Signo de Murphy", "Nausea y vómito"])
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
    with col2:
        Tipocxcardio = st.multiselect("Procedimientos cardiovasculares", [
                                      "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"])
st.subheader("Scores de ingreso")


#Bloque de código para SOFA score
#para un cuadro azul parecido a succes, error, y warningst.info("SOFA")
SOFA = '<p style="font-family:Times; color:Yellow; font-size: 30px;">SOFA</p>'
st.markdown(SOFA, unsafe_allow_html=True)
col1, col2, col3 = st.beta_columns(3)
with col1:
    PaO2 = st.number_input("PaO2 en mmHg", 1, None, 1)
with col2:
    FiO2 = st.number_input("FiO2 %", 1, None)
with col3:
    PAFI = (PaO2/FiO2)*100
    st.number_input("PAFI", None, None, PAFI)
col1, col2 = st.beta_columns(2)
with col1:
    ventmec = st.selectbox("¿Ventilación mecánica?", ["No", "Si"])

#Puntaje respiratorio
if PAFI > 400:
    PtResp = 0
    st.subheader("Respiratorio")
    st.success(PtResp)
elif PAFI < 400 and PAFI > 300:
    PtResp = 1
    st.subheader("Respiratorio")
    st.success(PtResp)
elif PAFI < 300 and ventmec == "No":
    PtResp = 2
    st.subheader("Respiratorio")
    st.warning(PtResp)
elif PAFI < 200 and PAFI > 100 and ventmec == "Si":
    st.subheader("Respiratorio")
    PtResp = 3
    st.warning(PtResp)
elif PAFI < 100 and ventmec == "Si":
    PtResp = 4
    st.subheader("Respiratorio")
    st.error(PtResp)

#Sección neurológica de SOFA

col1, col2 = st.beta_columns(2)
with col1:
    Glasgow = st.number_input("Escala de coma de Glasgow", 1, 15, 1, 1)
if Glasgow == 15:
    Ptneu = 0
    st.subheader("Neurológico")
    st.success(Ptneu)
elif Glasgow == 13 or Glasgow == 14:
    Ptneu = 1
    st.subheader("Neurológico")
    st.success(Ptneu)
elif Glasgow == 10 or Glasgow == 11 or Glasgow == 12:
    Ptneu = 2
    st.subheader("Neurológico")
    st.warning(Ptneu)
elif Glasgow >= 6 and Glasgow <= 9:
    Ptneu = 3
    st.subheader("Neurológico")
    st.warning(Ptneu)
elif Glasgow < 6:
    Ptneu = 4
    st.subheader("Neurológico")
    st.error(Ptneu)

glas = st.checkbox("Glasgow")
if glas == True:
    st.image("Glasgow.jpeg")

#Término de sección neurológica de SOFA

#Sección metabólica
Bilisingre = st.number_input("Bilirrubinas", None, None, 1.0, 0.1)
if Bilisingre < 1.2:
    st.subheader("Hígado")
    biling = 0
    st.success(biling)
elif Bilisingre > 1.2 and Bilisingre < 1.9:
    st.subheader("Hígado")
    biling = 1
    st.success(biling)
elif Bilisingre > 2 and Bilisingre <= 5.9:
    st.subheader("Hígado")
    biling = 2
    st.warning(biling)
elif Bilisingre >= 6.0 and Bilisingre <= 11.9:
    st.subheader("Hígado")
    biling = 3
    st.warning(biling)
elif Bilisingre >= 12:
    st.subheader("Hígado")
    biling = 4
    st.error(biling)

#Término de sección metabólica de SOFA

col1, col2, col3 = st.beta_columns(3)
with col1:
    sisting = st.number_input("Sistólica de ingreso", 1, None)
with col2:
    diasting = st.number_input("Diastólica de ingreso", 1, None)
with col3:
    PAMing = ((diasting+diasting)+sisting)/3
    IntPAMing = int(PAMing)
    prueba = st.number_input("PAM ingreso", None, None, IntPAMing)
vasopres= st.selectbox("Uso de vasopresores",["Sin vasopresor","Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis","Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min","Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min"])
if IntPAMing >70 and vasopres == "Sin vasopresor":
    st.subheader("Cardiovascular")
    carding = 0
    st.success(carding)
elif IntPAMing <70 and vasopres == "Sin vasopresor":
    st.subheader("Cardiovascular")
    carding = 1
    st.success(carding)
elif vasopres== "Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis":
    st.subheader("Cardiovascular")
    carding = 2
    st.warning(carding)
elif vasopres== "Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min":
    st.subheader("Cardiovascular")
    carding = 3
    st.warning(carding)
elif vasopres== "Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min":
    st.subheader("Cardiovascular")
    carding = 4
    st.error(carding)


col1, col2 = st.beta_columns(2)
with col1:
    plaqing = st.number_input("Plaquetas de ingreso x10*3/ml",1,1000,150,1)
    st.subheader("Coagulación")

if plaqing >= 150:
    sofplaqing=0
    with col1:
        st.success(sofplaqing)
elif plaqing <150 and plaqing >= 100:
    sofplaqing=1
    with col1:
        st.success(sofplaqing)
elif plaqing <=100 and plaqing >= 50:
    sofplaqing=2
    with col1:
        st.warning(sofplaqing)
elif plaqing <=50 and plaqing >= 20:
    sofplaqing=3
    with col1:
        st.warning(sofplaqing)
elif plaqing <=20:
    sofplaqing=4
    with col1:
        st.error(sofplaqing)

with col2:
    creating = st.number_input("Creatinina de ingreso mg/dl",1.0,10.0,1.0,0.1)
    uresissofaingre=st.number_input("Uresis/dia",1,100000,1,1)
    st.subheader("Renal")
if creating <1.2 and uresissofaingre >500:
    sofcreating=0
    with col2:
        st.success(sofcreating)
elif creating >1.2 and creating <1.9 and uresissofaingre >500:
    sofcreating=1
    with col2:
        st.success(sofcreating)
elif creating >2 and creating <3.4 and uresissofaingre >500:
    sofcreating=2
    with col2:
        st.warning(sofcreating)
elif creating >3.5 and creating <4.9 or uresissofaingre <500:
    sofcreating=3
    with col2:
        st.warning(sofcreating)
elif creating >=5 or uresissofaingre <200:
    sofcreating=4
    with col2:
        st.error(sofcreating)




#Puntaje de SOFA


#Termina bloque de código para SOFA score en streamlit

st.subheader("Postoperatorio")
#Variables del postoperatorio
