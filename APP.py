#Tesis de cirugía en pacientes con colecistitis alitiásica
import numpy
import pandas
import matplotlib
from PIL.Image import TRANSPOSE
import streamlit as st
from streamlit.widgets import NoValue
st.title("CxColCardio")
#'''Se buscará paciente con ID unico el NSS con agregado para no repetir el registro
#por lo que debe ser completado'''
nss=st.sidebar.text_input("Registrar paciente con NSS colocar agregado sin espacios")
NSS=nss.upper() #Hace el input de nss en mayuscular para que no falle el if con mayuscula
if NSS=="":
    st.image("CMN SXXI.jpeg",None,600,500)
    buscar=st.text_input("Busqueda de paciente")
elif NSS!="":
    st.sidebar.markdown("Registra los datos del nuevo paciente")
    st.sidebar.image("CMN SXXI.jpeg",None)
    col1,col2=st.beta_columns(2)
    with col1:
        nom=st.text_input("Nombre del paciente")
    with col2:
        edad=st.number_input("Edad",1,120,1)
    Genero="F" in NSS
    if Genero==True:
        #Para modificar el markdown con HTML se usa ese codigo de abajo
        #willkomen = '<p style="font-family:Times; color:Brown; font-size: 60px;">Bienvenida</p>'
        #st.markdown(willkomen, unsafe_allow_html=True)
        Genero="Femenino"
        st.write("Bienvenida",nom,"completemos el formulario")
    else:
        st.write("Bienvenido",nom,"completemos el formulario")
        Genero="Masculino"
    croni=st.multiselect("Enfermedades crónicas",["Diabetes mellitus","Hipertensión arterial","Valvulopatia","Cirugía de corazón","Infarto agudo al miocardio","Insuficiencia cardiaca","Otros"])
        
