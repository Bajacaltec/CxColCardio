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


    