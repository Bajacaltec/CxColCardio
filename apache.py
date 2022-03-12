#score de apacheII

def temp(temp):
    if temp >= 40.9:
        pttemp=4
    elif temp >=39 and temp <=40.89:
        pttemp=3
    elif temp>=38.5 and temp <=39.9:
        pttemp=1
    elif temp>=36 and temp <=38.4:
        pttemp=0
    elif temp>=34 and temp <=35.9:
        pttemp=1
    elif temp >=32 and temp <=33.9:
        pttemp=2
    elif temp >=30 and temp <=31.9:
        pttemp=3
    elif temp <=30:
        pttemp=4
def PAM(diasting,sisting):
    PAMing = ((diasting+diasting)+sisting)/3
    if PAMing>=159:
        ptpam=4
    elif PAMing>=130 and PAMing<=159:
        ptpam=3
    elif PAMing>=110 and PAMing<=129:
        ptpam=2
    elif PAMing>=70 and PAMing<=109:
        ptpam=0
    elif PAMing>=50 and PAMing<=69:
        ptpam=2
    elif PAMing<=50:
        ptpam=4
        
#APACHE frecuencia cardiáca falta

def fc(fc):
    if fc>=179:
        fcpt=4
    elif fc>=140 and fc <=179:
        fcpt=3
    elif fc >=110 and fc<=129:
        fcpt=2
    elif fc>=70 and fc<=109:
        fcpt=0
    elif fc>=55 and fc <=69:
        fcpt=2
    elif fc>=40 and fc<=54:
        fcpt=3
    elif fc<=50:
        fcpt=4

def fr(fr):
    if fr>=49:
        frpt=4
    elif fr>=35 and fr <=49:
        frpt=3
    elif fr>=25 and fr <=34:
        frpt=1
    elif fr>=12 and fr <=24:
        frpt=0
    elif fr>=10 and fr <=11:
        frpt=1
    elif fr >=6 and fr <=9:
        frpt=2
    elif fr <=6:
        fr=4
#Pendiente oxigenación no le entiendo :/

    