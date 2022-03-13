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

def ph(ph):
    if ph >=7.9:
        phpt=4
    elif ph>=7.6 and ph>=7.69:
        phpt=3
    elif ph>=7.5 and ph<=7.59:
        phpt=1
    elif ph>=7.33 and ph<=7.49:
        phpt=0
    elif ph>=7.25 and ph<=7.32:
        phpt=2
    elif ph>=7.15 and ph<=7.24:
        phpt=3
    elif ph<=7.15:
        phpt=4
def na(na):
    if na>=179:
        napt=4
    elif na>=160 and na<=179:
        napt=3
    elif na>=155 and na <=159:
        napt=2
    elif na>=150 and na<=154:
        napt=1
    elif na>=130 and na <=149:
        napt=0
    elif na>=120 and na <=129:
        napt=2
    elif na>=111 and na <=119:
        napt=3
    elif na<=111:
        napt=4
        
def k(k):
    if k>=6.9:
        kpt=4
    elif k>=6 and k<=6.9:
        kpt=3
    elif k>=5.5 and k<=5.9:
        kpt=1
    elif k>= 3.5 and k<=5.4:
        kpt=0
    elif k>=3 and k<=3.4:
        kpt=1
    elif k>=2.5 and k<=2.9:
        kpt=2
    elif k<=2.5:
        kpt=4

def creat(creat):
    if creat >=3.4:
        creatpt=4
    elif creat>=2.0 and creat <=3.4:
        creatpt=3
    elif creat >=1.5 and creat <=1.9:
        creatpt=2
    elif creat >=0.6 and creat <=1.4:
        creatpt=0
    elif creat <=0.6:
        creatpt=2
def hto(hto):
    if hto>=59.9:
        htopt=4
    elif hto>=50 and hto<=59.9:
        htopt=2
    elif hto>=46 and hto<=49.9:
        htopt=1
    elif hto>=30 and hto<=45.9:
        htopt=0
    elif hto>=20 and hto<=29.9:
        htopt=2
    elif hto<=20:
        htopt=4
def leu(leu):
    if leu>=39.9:
        leupt=4
    elif leu>=20 and leu<=39.9:
        leupt=2
    elif leu>=15 and leu<=19.9:
        leupt=1
    elif leu>=3 and leu<=14.9:
        leupt=0
    elif leu>=1 and leu<=2.9:
        leupt=2
    elif leu<=1
    leupt=4
    

    