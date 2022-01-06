#Tesis de cirugía en pacientes con colecistitis alitiásica
import streamlit as st
from streamlit.widgets import NoValue
st.title("CxColCardio")
#'''Se buscará paciente con ID unico el NSS con agregado para no repetir el registro
#por lo que debe ser completado'''
NSS=st.sidebar.number_input("NSS colocar agregado sin espacios",1,None,1,)
if NSS==1:
    st.image("CMN SXXI.jpeg",None)

