import streamlit as st
# ---------------------------------------------------------------------------- #
#                             Puntaje respiratorio                             #
# ---------------------------------------------------------------------------- #
def Resp(PaO2,FiO2,ventmec):
    PAFI = (PaO2/FiO2)*100
    #Puntaje respiratorio
    if PAFI >= 400 and ventmec=="No":
        Resp.PtResp = 0
    elif PAFI < 400 and PAFI >= 300 and ventmec=="No":
        Resp.PtResp = 1
    elif PAFI < 300 and ventmec == "No":
        Resp.PtResp = 2
    #Revisar la escala por que hay un hueco desde el  menos de 300 al 200 con ventilación mecánica que no definen cual es el puntaje
    elif PAFI <= 299 and PAFI >= 100 and ventmec == "Si":
        Resp.PtResp = 3
    elif PAFI < 100 and ventmec == "Si":
        Resp.PtResp = 4
    #Pasar esto al final en una tabla final para resultado de puntajes y PAFI
# ---------------------------------------------------------------------------- #
#                              Puntaje neurológico                             #
# ---------------------------------------------------------------------------- #
def Neu(Glasgow):
    if Glasgow == 15:
        Neu.Ptneu = 0
    elif Glasgow == 13 or Glasgow == 14:
        Neu.Ptneu = 1
    elif Glasgow == 10 or Glasgow == 11 or Glasgow == 12:
        Neu.Ptneu = 2
    elif Glasgow >= 6 and Glasgow <= 9:
        Neu.Ptneu = 3
    elif Glasgow < 6:
        Neu.Ptneu = 4
    glas = st.checkbox("Glasgow")
    if glas == True:
        st.image("Glasgow.jpeg")

# ---------------------------------------------------------------------------- #
#                                Metabólica SOFA                               #
# ---------------------------------------------------------------------------- #
def metabol(Bilisingre):
    if Bilisingre < 1.2:
        metabol.biling = 0
    elif Bilisingre > 1.2 and Bilisingre < 1.9:
        metabol.biling = 1
    elif Bilisingre > 2 and Bilisingre <= 5.9:
        metabol.biling = 2
    elif Bilisingre >= 6.0 and Bilisingre <= 11.9:
        metabol.biling = 3
    elif Bilisingre >= 12:
        metabol.biling = 4
   
# ---------------------------------------------------------------------------- #
#                                Cardiovascular                                #
# ---------------------------------------------------------------------------- #
def cardio(diasting,sisting):
    PAMing = ((diasting+diasting)+sisting)/3
    IntPAMing = int(PAMing)
    vasopres= st.selectbox("Uso de vasopresores",["Sin vasopresor","Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis","Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min","Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min"])
    if IntPAMing >70 and vasopres == "Sin vasopresor":
        cardio.carding = 0
    elif IntPAMing <70 and vasopres == "Sin vasopresor":
        cardio.carding = 1
    elif vasopres== "Dopamina < o = a 5 mcg/kg/min o dobutamina cualquier dósis":
        cardio.carding = 2
    elif vasopres== "Dopamina > 5mcg/kg/min o epinefrina <0.1 mcg/kg/min o norepinefrina <0.1mcg/kg/min":
        cardio.carding = 3
    elif vasopres== "Dopamina >15 mcg/kg/min o epinefrina o norepinefrina >0.1 mcg/kg/min":
        cardio.carding = 4
   

# ---------------------------------------------------------------------------- #
#                                  Coagulación                                 #
# ---------------------------------------------------------------------------- #
def coag(plaqing):
    if plaqing >= 150:
        coag.sofplaqing=0
    elif plaqing <150 and plaqing >= 100:
        coag.sofplaqing=1
    elif plaqing <=100 and plaqing >= 50:
        coag.sofplaqing=2
    elif plaqing <=50 and plaqing >= 20:
        coag.sofplaqing=3
    elif plaqing <=20:
        coag.sofplaqing=4
   

# ---------------------------------------------------------------------------- #
#                                   urinario                                   #
# ---------------------------------------------------------------------------- #
def urin(creating,uresisingre):
    if creating <1.2 and uresisingre >500:
        urin.sofcreating=0
    elif creating >1.2 and creating <1.9 and uresisingre >500:
        urin.sofcreating=1
    elif creating >2 and creating <3.4 and uresisingre >500:
        urin.sofcreating=2
    elif creating >3.5 and creating <4.9 or uresisingre <500:
        urin.sofcreating=3
    elif creating >=5 or uresisingre <200:
        urin.sofcreating=4
   
