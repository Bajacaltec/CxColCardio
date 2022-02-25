#APACHE II
import streamlit as st

# ---------------------------------------------------------------------------- #
#                             Puntaje respiratorio                             #
# ---------------------------------------------------------------------------- #
def Resp(PaO2,FiO2,ventmec):
    PAFI = (PaO2/FiO2)*100
    #Puntaje respiratorio
    if PAFI >= 400 and ventmec=="No":
        PtResp = 0
    elif PAFI < 400 and PAFI >= 300 and ventmec=="No":
        PtResp = 1
    elif PAFI < 300 and ventmec == "No":
        PtResp = 2
    #Revisar la escala por que hay un hueco desde el  menos de 300 al 200 con ventilación mecánica que no definen cual es el puntaje
    elif PAFI <= 299 and PAFI >= 100 and ventmec == "Si":
        PtResp = 3
    elif PAFI < 100 and ventmec == "Si":
        PtResp = 4
    #Pasar esto al final en una tabla final para resultado de puntajes y PAFI
    st.text(PAFI)
    st.text(PtResp)
# ---------------------------------------------------------------------------- #
#                              Puntaje neurológico                             #
# ---------------------------------------------------------------------------- #
def Neu(Glasgow):
    if Glasgow == 15:
        Ptneu = 0
    elif Glasgow == 13 or Glasgow == 14:
        Ptneu = 1
    elif Glasgow == 10 or Glasgow == 11 or Glasgow == 12:
        Ptneu = 2
    elif Glasgow >= 6 and Glasgow <= 9:
        Ptneu = 3
    elif Glasgow < 6:
        Ptneu = 4
    st.write(Glasgow)
    glas = st.checkbox("Glasgow")
    if glas == True:
        st.image("Glasgow.jpeg")

# ---------------------------------------------------------------------------- #
#                                Metabólica SOFA                               #
# ---------------------------------------------------------------------------- #
def metabolica(Bilisingre):
    if Bilisingre < 1.2:
        biling = 0
    elif Bilisingre > 1.2 and Bilisingre < 1.9:
        biling = 1
    elif Bilisingre > 2 and Bilisingre <= 5.9:
        biling = 2
    elif Bilisingre >= 6.0 and Bilisingre <= 11.9:
        biling = 3
    elif Bilisingre >= 12:
        biling = 4
    st.write("Las bilis son")
    st.write(biling)


