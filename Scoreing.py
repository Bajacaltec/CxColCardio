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

# ---------------------------------------------------------------------------- #
#                                Cardiovascular                                #
# ---------------------------------------------------------------------------- #
def cardio(diasting,sisting):
    PAMing = ((diasting+diasting)+sisting)/3
    IntPAMing = int(PAMing)
    vasopres= st.selectbox("Uso de vasopresores",["Sin vasopresor","Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis","Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min","Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min"])
    if IntPAMing >70 and vasopres == "Sin vasopresor":
        st.subheader("Cardiovascular")
        carding = 0
    elif IntPAMing <70 and vasopres == "Sin vasopresor":
        st.subheader("Cardiovascular")
        carding = 1
    elif vasopres== "Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis":
        st.subheader("Cardiovascular")
        carding = 2
    elif vasopres== "Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min":
        st.subheader("Cardiovascular")
        carding = 3
    elif vasopres== "Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min":
        st.subheader("Cardiovascular")
        carding = 4
    st.write("Cardio")
    st.write(carding)

# ---------------------------------------------------------------------------- #
#                                  Coagulación                                 #
# ---------------------------------------------------------------------------- #
def coagulacion(plaqing):
    if plaqing >= 150:
        sofplaqing=0
    elif plaqing <150 and plaqing >= 100:
        sofplaqing=1
    elif plaqing <=100 and plaqing >= 50:
        sofplaqing=2
    elif plaqing <=50 and plaqing >= 20:
        sofplaqing=3
    elif plaqing <=20:
        sofplaqing=4
    st.write("Plaquetas")
    st.write(sofplaqing)

# ---------------------------------------------------------------------------- #
#                                   urinario                                   #
# ---------------------------------------------------------------------------- #
def urinario(creating,uresisingre):
    if creating <1.2 and uresisingre >500:
        sofcreating=0
    elif creating >1.2 and creating <1.9 and uresisingre >500:
        sofcreating=1
    elif creating >2 and creating <3.4 and uresisingre >500:
        sofcreating=2
    elif creating >3.5 and creating <4.9 or uresisingre <500:
        sofcreating=3
    elif creating >=5 or uresisingre <200:
        sofcreating=4
    st.write('uresis')
    st.write(sofcreating)
