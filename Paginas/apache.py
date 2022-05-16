#score de apacheII
import streamlit as st
def tempdef(temp):
    if temp >= 40.9:
        tempdef.pttemp=4
    elif temp >=39 and temp <=40.89:
        tempdef.pttemp=3
    elif temp>=38.5 and temp <=39.9:
        tempdef.pttemp=1
    elif temp>=36 and temp <=38.4:
        tempdef.pttemp=0
    elif temp>=34 and temp <=35.9:
        tempdef.pttemp=1
    elif temp >=32 and temp <=33.9:
        tempdef.pttemp=2
    elif temp >=30 and temp <=31.9:
        tempdef.pttemp=3
    elif temp <=30:
        tempdef.pttemp=4
def PAM(diasting,sisting):
    PAMing = ((diasting+diasting)+sisting)/3
    if PAMing>=159:
        PAM.ptpam=4
    elif PAMing>=130 and PAMing<=159:
        PAM.ptpam=3
    elif PAMing>=110 and PAMing<=129:
        PAM.ptpam=2
    elif PAMing>=70 and PAMing<=109:
        PAM.ptpam=0
    elif PAMing>=50 and PAMing<=69:
        PAM.ptpam=2
    elif PAMing<=50:
       PAM.ptpam=4
        
def fcdef(fc):
    if fc>=179:
        fcdef.fcpt=4
    elif fc>=140 and fc <=179:
        fcdef.fcpt=3
    elif fc >=110 and fc<=129:
        fcdef.fcpt=2
    elif fc>=70 and fc<=109:
        fcdef.fcpt=0
    elif fc>=55 and fc <=69:
        fcdef.fcpt=2
    elif fc>=40 and fc<=54:
        fcdef.fcpt=3
    elif fc<=50:
        fcdef.fcpt=4

def frdef(fr):
    if fr>=49:
        frdef.frpt=4
    elif fr>=35 and fr <=49:
        frdef.frpt=3
    elif fr>=25 and fr <=34:
        frdef.frpt=1
    elif fr>=12 and fr <=24:
        frdef.frpt=0
    elif fr>=10 and fr <=11:
        frdef.frpt=1
    elif fr >=6 and fr <=9:
        frdef.frpt=2
    elif fr <=6:
        frdef.fr=4

def oxigen(fio2,aaDO2,pao2):
    if fio2>=50:
        if aaDO2>=499:
            oxigen.opt=4
        elif aaDO2>=350 and aaDO2<=499:
            oxigen.opt=3
        elif aaDO2>=200 and aaDO2<=349:
            oxigen.opt=2
        elif aaDO2<=200:
            oxigen.opt=0
    elif fio2<=50:
        if pao2>=70:
            oxigen.opt=0
        elif pao2>=61 and pao2<=70:
            oxigen.opt=1
        elif pao2>=55 and pao2<=60:
            oxigen.opt=3
        elif pao2<55:
            oxigen.opt=4
        
        
            
        
        
def phdef(ph):
    if ph >=7.9:
        phdef.phpt=4
    elif ph>=7.6 and ph>=7.69:
        phdef.phpt=3
    elif ph>=7.5 and ph<=7.59:
        phdef.phpt=1
    elif ph>=7.33 and ph<=7.49:
        phdef.phpt=0
    elif ph>=7.25 and ph<=7.32:
        phdef.phpt=2
    elif ph>=7.15 and ph<=7.24:
        phdef.phpt=3
    elif ph<=7.15:
        phdef.phpt=4
def nadef(na):
    if na>=179:
        nadef.napt=4
    elif na>=160 and na<=179:
        nadef.napt=3
    elif na>=155 and na <=159:
        nadef.napt=2
    elif na>=150 and na<=154:
        nadef.napt=1
    elif na>=130 and na <=149:
        nadef.napt=0
    elif na>=120 and na <=129:
        nadef.napt=2
    elif na>=111 and na <=119:
        nadef.napt=3
    elif na<=111:
        nadef.napt=4
        
def kdef(k):
    if k>=6.9:
        kdef.kpt=4
    elif k>=6 and k<=6.9:
        kdef.kpt=3
    elif k>=5.5 and k<=5.9:
        kdef.kpt=1
    elif k>= 3.5 and k<=5.4:
        kdef.kpt=0
    elif k>=3 and k<=3.4:
        kdef.kpt=1
    elif k>=2.5 and k<=2.9:
        kdef.kpt=2
    elif k<=2.5:
        kdef.kpt=4

def creatdef(creat):
    if creat >=3.4:
        creatdef.creatpt=4
    elif creat>=2.0 and creat <=3.4:
        creatdef.creatpt=3
    elif creat >=1.5 and creat <=1.9:
        creatdef.creatpt=2
    elif creat >=0.6 and creat <=1.4:
        creatdef.creatpt=0
    elif creat <=0.6:
        creatdef.creatpt=2
def htodef(hto):
    if hto>=59.9:
        htodef.htopt=4
    elif hto>=50 and hto<=59.9:
        htodef.htopt=2
    elif hto>=46 and hto<=49.9:
        htodef.htopt=1
    elif hto>=30 and hto<=45.9:
        htodef.htopt=0
    elif hto>=20 and hto<=29.9:
        htodef.htopt=2
    elif hto<=20:
        htodef.htopt=4
def leut(leu):
    if leu>=39.9:
        leut.leupt=4
    elif leu>=20 and leu<=39.9:
        leut.leupt=2
    elif leu>=15 and leu<=19.9:
        leut.leupt=1
    elif leu>=3 and leu<=14.9:
        leut.leupt=0
    elif leu>=1 and leu<=2.9:
        leut.leupt=2
    elif leu<=1:
        leut.leupt=4
def cronic(comorb):
    print("")
    #Ver lo de los crónicos como se califica
    
def edas(edad):
    if edad<=44:
        edas.edadpt=0
    elif edad>=45 and edad <=64:
        edas.edadpt=1
   # elif edad>=55 and edad <=64: #parece un erro en el puntaje de edad
    #    edadpt=2
    elif edad>=65 and edad<=74:
        edas.edadpt=5
    elif edad>=75:
        edas.edadpt=6
        
def cronicos(cronicosapache):
    with st.expander('APACHE II'):
        if cronicos!="":
            estadoqx=st.selectbox("Estado",['No quirúrgico','Programado','Urgencia'])
            if estadoqx=='No quirúrgico':
                cronicos.ptestado=5
            elif estadoqx=='Programado':
                cronicos.ptestado=2
            elif estadoqx=='Urgencia':
                cronicos.ptestado=5
def cronicospreqx(estadoqx):
            if estadoqx=='No quirúrgico':
                cronicos.ptestado=5
            elif estadoqx=='Programado':
                cronicos.ptestado=2
            elif estadoqx=='Urgencia':
                cronicos.ptestado=5
