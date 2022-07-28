from sqlalchemy import true
import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
from Paginas.SOFAing import Neu, Resp, cardio, coag, metabol, urin
from itertools import chain
from Paginas.apache import PAM, creatdef, cronicos, cronicospreqx, edas, fcdef, htodef, kdef, leut, nadef, oxigen,frdef, phdef
from Paginas.apache import tempdef
from Paginas.censo import insertar


def base():
    col1,col2=st.columns(2)
    with col1:
        with st.expander('Identificación y somatometría',True):
            con = sqlite3.connect('DB.db')
            cur = con.cursor()

            sumedad=cur.execute('''Select Nombre FROM Basecxcol''')
            nom=cur.fetchall()
            res = []
            for i in chain(*nom):
                res.append(i)
            
            nombre=(st.selectbox('Nombre',res), )
            nambre=str(nombre)
            numbre=nambre.replace("('","")
            global nimbre
            nimbre=(numbre.replace("',)",""),)
            con.close()

            cen = sqlite3.connect('DB.db')
            cor = cen.cursor()
            cor.execute("SELECT * FROM Basecxcol WHERE Nombre=(?)",(nimbre))
            global bes
            bes,=cor.fetchall()
            
            cen.commit()
            cen.close()
            st.sidebar.write(list(bes))
            global NSS
            NSS=st.text_input("NSS",bes[2])
            global edad
            Genero = "F" in NSS
            if Genero == True:
                Gen = "Femenino"
            else:
                Gen = "Masculino"
            bestrim_edad=int(bes[1])
            edad=st.number_input('Edad',1,200,bestrim_edad,key='987')
            bestrim_peso=int(bes[3])
            global peso
            peso = st.number_input("Peso",1,800,bestrim_peso,key='829')
            global talla
            bestrim_talla=float(bes[4])
            talla = st.number_input("Talla", 0.1, None, bestrim_talla, 0.1)
            bestrim_imc=float(bes[5])
            global imc
            indiceMC = st.number_input("IMC",None,None,bestrim_imc,0.1,disabled=True)
            st.success('')
        
    with col2:
        with st.expander('Comentarios'):
            con=sqlite3.connect('DB.db')
            cur=con.cursor()
            cur.execute("SELECT Comentarios FROM Basecxcol WHERE NSS=?",(NSS,))
            coment_base,=cur.fetchone()
            coment=st.text_area('Actualizar comentario',coment_base,350)
            actual_boton=st.button('Actualizar')
            if actual_boton==True:
                con=sqlite3.connect('DB.db')
                cur=con.cursor()
                cur.execute("""UPDATE Basecxcol SET Comentarios2=? WHERE NSS=?""",(coment,NSS))
                st.success('Actualizado')
                con.commit()
                con.close()
            
    with st.expander('Antecedentes'):
        col1,col2,col3=st.columns(3)
        with col1:
            global comor
            comor_1=str(bes[6])
            comor_a=comor_1.replace("['","")
            comor_b=comor_a.replace(" '","")
            comor_c=comor_b.replace("]","")
            comor_d=comor_c.replace("'","")
            comor_f=comor_d.replace("[","")
            comor_final=comor_f.split(",")
            
            comor=st.multiselect("Enfermedades crónicas", ["",'Bloqueo auriculoventricular','Dislipidemias','Linfoma','Fibrilación auricular',"Diabetes mellitus", "Hipertensión arterial", "Valvulopatia","Cirugía de corazón", "Infarto agudo al miocardio", "Insuficiencia cardiaca", "Miocarditis","Miocardiopatia dilatada",'Estenosis mitral',"Otros"],comor_final) 
        with col2:
            global tab
            tab_1=bes[7]
            if tab_1=='Si':
                tab_index=1
            elif tab_1=='No':
                tab_index=0
            tab=st.selectbox("Tabaquismo",['No','Si'],index=tab_index)
            if tab=='Si':
                global cajetillas
                cajetillas=st.number_input("Cajetillas/año",1,7000,bes[8],1)
            else:
                cajetillas='NA'
            global cronicosapache
        with col3:
            #Conversion de los adtos de la base de datos a texto para que se precarguen cmo una lista en el multiselect
            try:
                cron_1=str(bes[10])
                cron_a=cron_1.replace("['","")
                cron_b=cron_a.replace("']","")
                cron_final=cron_b.split(",")
                cronicosapache=st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos'],cron_final)
            except:
                cronicosapache=st.multiselect('Enfermedades crónicas para APACHEII',['Ninguna','Cirrosis confirmada (biopsia) ', 'NYHA Clase IV','EPOC Grave (ej. Hipercapnia, O2 domiciliario, HT pulmonar)','Diálisis crónica','Inmunocomprometidos'])

        with col1:
            global Tipocxcardio
            try:
                cxcardio_1=str(bes[13])
                cxcardio_a=cxcardio_1.replace("['","")
                cxcadio_b=cxcardio_a.replace("']","")
                cx_cardiofinal=cxcadio_b.split(",")
                
                Tipocxcardio =st.multiselect("Procedimientos cardiovasculares", ['Disminución de clase funcional ICC','Infarto agudo al miocardio',
                                            "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular",'Colocación de marcapaso'],cx_cardiofinal)
            except:
                Tipocxcardio =st.multiselect("Procedimientos cardiovasculares", ['Disminución de clase funcional ICC','Infarto agudo al miocardio',
                                            "Cirugia cardiovascular", "Cateterismo cardiaco", "Reemplazo valvular"])
        with col2:
            global usovasopr
            vasopres_1=bes[11]
            if vasopres_1=='Si':
                index_vasopres=1
            elif vasopres_1=='No':
                index_vasopres=0
            else:
                index_vasopres=0
            usovasoping=st.selectbox("Uso de vasopresores previos a cirugía por CCLA", ["No", "Si"],index=index_vasopres)
            
            if usovasoping == "Si":

                try:
                    global tipovasopr
                    tipovaso_1=str(bes[12])
                    tipo_vaso_a=tipovaso_1.replace("['","")
                    tipo_vaso_b=tipo_vaso_a.replace("']","")
                    tipo_vaso_final=tipo_vaso_b.split(",")
                    tipovasopring = st.multiselect("Que vasopresor se utilizó", ["Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"],tipo_vaso_final)
                    tipovasopringd=str(tipovasopring)
                    st.success('')

                except:
                    tipovasopring = st.multiselect("Que vasopresor se utilizó", ["Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
                    tipovasopringd=str(tipovasopring)
                    st.error('')


            else:
                tipovasopring='NA'
                tipovasopringd=str(tipovasopring)

        with col3:
            global ventprol
            try:
                ventprol = st.number_input(
                    "Días con ventilación mecánica previo a cirugía", 0, 100, bes[9], 1)
            except:
                ventprol = st.number_input(
                    "Días con ventilación mecánica previo a cirugía", 0, 100, 0, 1)
        with col1:
            try:
                uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,bes[38],1)
            except:
                uciestpreop=st.number_input("Dias de estancia en UCI previo a cirugía",0,300,0,1)
                            
                            #Signos vitales de ingreso
        vol1,vol2,vol3,vol4=st.columns(4)
        with vol1:
            global FC
            FC=st.number_input("FC/min",1,300,bes[14])
        with vol2:
            global FR
            FR=st.number_input("Fr/min",1,300,bes[15],1)
        with vol3:
            global Sisting
            Sisting=st.number_input('Sistólica',1,300,bes[16],110)
        with vol4:
            global Diasting
            Diasting=st.number_input('Diastólica',1,300,bes[17],1)
        with vol1:
            global Temping
            Temping=st.number_input('T°C',34.1,45.1,bes[18],0.1)
            
    #Sección de laboratorios
    with st.expander('Laboratorios de ingreso'):
        sol1,sol2,sol3,sol4=st.columns(4)
        with sol1:
            global ADE
            ADE=st.number_input("ADE",0,1000,bes[21])
        with sol2:
            global PCR
            PCR=st.number_input("PCR mg/dl",key='<pcr>',value=bes[22])
        with sol3:
            global AST
            AST=st.number_input("AST",0,100000,key='<ast>',value=bes[23])
        with sol4:
            global ALT
            ALT=st.number_input("ALT ",0,100000,value=bes[24])
        with sol1:
            global Bil
            Bil=st.number_input("Bil tot ",0.0,100.1,bes[25],0.1)
        with sol2:
            global FA
            FA=st.number_input("FA ",0,value=bes[26])
        with sol3:
            global INR
            INR=st.number_input("INR ",0.0,100.1,bes[27],0.1)
        with sol4:
            global GGT
            GGT=st.number_input("GGT ",0,value=bes[28])
        with sol1:
            global NA
            NA=st.number_input('Sodio',1,200,bes[32])
        with sol2:
            global K
            K=st.number_input('Potasio ',value=bes[29])
        
        with sol4:
            global Hto
            Hto=st.number_input("Hematocrito ",1,100,bes[31])
        with sol3:
            global creating
            creating=st.number_input("Creatinina ",value=bes[34])
        with sol2:
            global Leuc
            Leuc=st.number_input("Leucocitos ",1,1000000000,bes[33])
        with sol4:
            global plaqing
            plaqing=st.number_input("Plaquetas",1,value=bes[35])
        with sol1:
            global pHing
            pHing=st.number_input('pH en gasometría de ingreso')
            
            
    #Sintomas de CCLA
    with st.expander('Síntomas de CCLA'):
        col1, col2 = st.columns(2)
        with col1:
            sinccla=str(bes[44])
            sintccla_x=sinccla.replace("['","")
            sintccla_b=sintccla_x.replace("']","")
            sintccla_c=sintccla_b.replace(" '","")
            sinccld=sintccla_c.replace("'","")
            sint_cclafinal=sinccld.split(",")
            global sysint
            sysint = st.multiselect('Sintomas compatibles',["[]","Dolor en hipocondrio derecho", "Vesícula palpable","Signo de Murphy", "Nausea y vómito","Ictericia","Fiebre","Dolor abdominal difuso","Estreñimiento"],sint_cclafinal)
        with col2:
            global usghall
            usg_a=str(bes[45])
            usgb=usg_a.replace(" '","")
            usgc=usgb.replace("[","")
            usgd=usgc.replace("]","")
            usgde=usgd.replace("'","")
            usg_e=usgde.split(",")
            usghall = str(st.multiselect("Hallazgos de ultrasonido",['','Líquido libre',"Engrosamiento de pared", "Líquido perivesicular", "Litiasis vesicular",
                                        "Distensión vesicular", "Gas intravesicular", "Lodo biliar", "Absceso perivesicular", "Anormalidad anatomíca","Dilatación de vía biliar"],usg_e))
            #pendiente autocarga da hallazgos tomográficos
            tac_a=str(bes[47])
            st.write(tac_a)
            tac_b=tac_a.replace("['","")
            tac_c=tac_b.replace("']","")
            tac_d=tac_c.replace(" '","")
            tac_f=tac_d.replace("'","")
            tac_e=tac_f.split(",")          
            tachall= st.multiselect("Hallazgos tomográficos",["","[]",'Distensión vesicular',"Litiasis vesicular","Hidrocolecisto","Litiasis vesicular","Lito en vía biliar","Dilatación de la vía biliar","Estriación de la grasa perivesicular","Engrosamiento de la pared","Líquido perivesicular","Pérdida de la captación del contraste","Gas dentro de la vesícula biliar","Estriación de la grasa perivesícular","Reforzamiento de la pared vesícular"],tac_e)
        with col1:
            global asa
            asa_a=(bes[46])
            if asa_a=='I':
                index_asa=0
            elif asa_a=='II':
                index_asa=1
            elif asa_a=='III':
                index_asa=2
            elif asa_a=='IV':
                index_asa=3
            elif asa_a=='V':
                index_asa=4
            elif asa_a=='VI':
                index_asa=5
            st.sidebar.write(asa_a)
            asa=str(st.selectbox("ASA", ["I", "II", "III", "IV", "V", "VI"],index_asa))
            asacheck = st.checkbox("ASA clasificación")
            if asacheck == True:
                st.image("/Users/alonso/CxColCardio/Paginas/Imagenes/ASA.png")
        col1, col2 = st.columns(2)
        with col1:
            sevcole_1=bes[48]
            if sevcole_1=='Leve':
                sev=0
            elif sevcole_1=='Moderado':
                sev=1
            elif sevcole_1=='Severo':
                sev=2
            global sevcole
            sevcole = str(st.selectbox("Severidad (Tokio 18)", [
                                    "Leve", "Moderado", "Severo"],sev))
            tokio = st.checkbox("Clasificación de Tokio 18")
            if tokio == True:
                st.image("/Users/alonso/CxColCardio/Paginas/Imagenes/Tokio.png")
        
        
    with st.expander('Signos vitales prequirúrgicos'):
        vol1,vol2,vol3,vol4=st.columns(4)
        with vol1:
            FCqx=st.number_input("FCpreqx/min",1,300,80,1)
        with vol2:
            FRqx=st.number_input("Frpreqx/min",1,300,20,1)
        with vol3:
            Sistingqx=st.number_input('Sistólicapreqx',1,300,110,1)
        with vol4:
            Diastqx=st.number_input('Diastólicapreqx',1,300,80,1)
        with vol1:
            Tempqx=st.number_input('T°Cpreqx',34.1,45.1,37.1,0.1)

            
    with st.expander('Laboratorios previos a la cirugía'):
    
        tol1,tol2,tol3,tol4=st.columns(4)
        with tol1:
            global ADEcx
            ADEcx=st.number_input("ADE",0,100,bes[49])
        with tol2:
            global PCRcx
            PCRcx=st.number_input(("PCR mg/dl"),0.1,700.0,bes[50],0.1)
        with tol3:
            global Leucx
            Leucx=st.number_input("Leucocitos mm3",0,100000,bes[51])
        with tol4:
            global ASTcx
            ASTcx=st.number_input("AST",0,13000,bes[52])
        with tol1:
            global ALTcx
            ALTcx=st.number_input("ALT",0,1092309,bes[53])
        with tol2:
            global Bilcx
            Bilcx=st.number_input("Bilirrubinas totales",0.0,100.1,bes[54])
        with tol3:
            global FAcx
            FAcx=st.number_input("FA",0,100000000,bes[55])
        with tol4:
            global INRcx
            INRcx=st.number_input("INR",0.0,100.1,bes[56])
        with tol1:
            global GGTcx
            GGTcx=st.number_input("GGT",0,12309013290,bes[57])
        with tol2:
            global NAcx
            NAcx=st.number_input('Sodio',0,10209210,bes[61])
        with tol3:
            global Kcx
            Kcx=st.number_input('Potasio',value=bes[58])
        with tol4:
            global pHcx
            pHcx=st.number_input("PH",0.0, 8.5,bes[59])
        with tol1:
            global Htocx
            Htocx=st.number_input("Hematocrito",0,100,bes[60])
        with tol2:
            global Creatcx
            Creatcx=st.number_input("Creatinina",0.0,10.1,bes[62])
        with tol4:
            global plaqqx
            plaqqx=st.number_input("Plaquetaspreqx",0,1000000,bes[89])
        
    with st.expander("Datos de la cirugía"):
        col1,col2=st.columns(2)
        with col1:
            global tiempevolcx
            tiempevolcx=st.number_input("Tiempo desde el inicio de los síntomas al tratamiento quirúrgico",0,600,bes[63],1)
            global duracioncx
            duracioncx=st.number_input("Duración de la cirugía (minutos)",1,700000,bes[65],1)
            recurrencia=st.checkbox("Recurrencia de lo síntomas")
            
            global hallazgos
            hall_a=str(bes[80])
            hall_b=hall_a.replace("['","")
            hall_c=hall_b.replace(" '","")
            hall_d=hall_c.replace("]","")
            hall_h=hall_d.replace("'","")
            hall_e=hall_h.split(",")
            
            hallazgos=str(st.multiselect('Hallazgos quirúrgicos',["","None",'Litiasis vesicular','Trombosis de artería cística','Distensión vesicular','Absceso perivesicular','Piocolecisto','Engrosamiento de pared','Necrosis de cístico','Líquido perivesicular','Absceso hepático','necrosis vesicular','perforación vesicular'],hall_e))
        with col2:
            tip=str(bes[64])
            if tip=='Laparoscopica':
                tipcx=0
            elif tip=='Abierta':
                tipcx=1
            tipocx=st.selectbox("Tipo de cirugía (abierta o laparoscopica)",["Laparoscopica","Abierta"],tipcx)
            global convcx
            convcx=st.checkbox("Conversión de cirugía laparoscopica a abierta",bes[66])
            global timeppostqx
            timeppostqx=st.number_input("Días de estancia posterior a tratamiento quirúrgico de colecistitis",1,60000,bes[67],1)
            
            ####### continuar aquí
        with col1:
            vaso=bes[68]
            if vaso =='No':
                vespt=0
            elif vaso=='Si':
                vespt=1
            usovasopr = st.selectbox("Uso de vasopresores", ["No", "Si"],key='>Postqxvasopres',index=vespt)
            if usovasopr == "Si":
                tipovasopr = st.multiselect("Que vasopresor se utilizó postqx", [
                                            "Dopamina", "Dobutamina", "Noradrenalina", "Vasopresina"])
            else:
                tipovasopr= "NA"
        with col2:
            ventprolposqx = st.number_input("Días con ventilación mecánica", 0, 100, bes[70], 1,key='<Postqxventilación>')
            uciestposqx=st.number_input("Dias de estancia en UCI postquirúrgico",0,300,bes[71],1,key='<uci>')
        with col1:
            global compli
            clavien=bes[69]
            if clavien=='I':
                clavpt=0
            elif clavien=='II':
                clavpt=1
            elif clavien=='III':
                clavpt=2
            elif clavien=='IV':
                clavpt=3
            elif clavien=='V':
                clavpt=4
            compli = st.selectbox("Complicaciones postoperatorias (Clavien-Dindo", ["I", "II", "III", "IV", "V"],key='<estamera>',index=clavpt)
            dindo=st.checkbox('Clasificación Clavien-dindo')
            if dindo==True:
                st.image('clavien.png')
       
        with col1:
            global lit
            try:
                tipolit=bes[79]
                if tipolit=='Litiasica':
                    tipolitpt=0
                elif tipolit=='Alitiasica':
                    tipolitpt=1
                lit=st.selectbox('Litiasica vs alitiasica',['Litiasica','Alitiasica'],tipolitpt)
            except:
                lit=st.selectbox('Litiasica vs alitiasica',['Litiasica','Alitiasica'])
                st.error("")
            global mort
            mortpt=bes[73]
            if mortpt=='No':
                morte=0
            elif mortpt=='Si':
                morte=1
            
            mort=st.selectbox("Muerte en los primeros 30 días posquirúrgicos",["No","Si"],morte)
            comord=str(comor)
            Tipocxcardiod=str(Tipocxcardio)
            sisintstr=str(sysint)
            tachalld=str(tachall)
            tipovasoprd=str(tipovasopr)
        modificar=st.button('Modificar')
        if modificar==True:
            con=sqlite3.connect('DB.db')
            cur=con.cursor()
            cur.execute("UPDATE Basecxcol SET Género= ? WHERE NSS = ?",(Gen,NSS))
            cur.execute("""UPDATE Basecxcol SET Edad= ?,Peso=?,Talla=?,IMC=?,Crónicos=?,Tabaquismo=?,Cajetillas=?,Diasventmec=?,Vasopresores=?,
                        Tipovasopresor=?,PRoccardio=?,FCing=?,FRing=?,Sising=?,Diasing=?,Temping=?,ADEing=?,
                        PCRing=?,ASTing=?,ALTing=?,Biltoting=?,FAing=?,INRing=?,GGTing=?,
                        King=?,PHing=?,Hematocritoing=?,Naing=?,Leuing=?,Plaquetasing=?,
                        UCIing=?,Sintomascompatccla=?,Hallazusg=?,asa=?,Hallazgtom=?,
                        Tokyo=?,ADEpreqx=?,Leupreqx=?,ASTpreqx=?,ALTpreqx=?,Biltotpreqx=?,
                        FApreqx=?,INRpreqx=?,GGTpreqx=?,Kpreqx=?,PHpreqx=?,HTOpreqx=?,NApreqx=?,Creatpreqx=?,Tiempoinsintqx=?,tipoqx=?,Duracionqx=?,Conversión=?,
                        Diasestancia=?,postqxvasopresor=?,Comppostqx=?,Ventmecpostqx=?,DiasUCIpreqx=?,Recurrsint=?,Muerte=?,Tipoccla=?,Hallazgoscx=?,
                        Fcpreqx=?,Frpreqx=?,Sistpreqx=?,Diastpreqx=?,Temppreqx=?,Tipovasoprexposqx=?,
                        Plaqpreqx=? WHERE NSS = ?""",(edad,peso,talla,indiceMC,comord,tab,cajetillas,ventprol,usovasoping,tipovasopringd,Tipocxcardiod,FC,FR,Sisting,Diasting,Temping,
                        ADE,PCR,AST,ALT,Bil,FA,INR,GGT,K,pHing,Hto,NA,Leuc,plaqing,uciestpreop,sisintstr,usghall,asa,tachalld,sevcole,ADEcx,Leucx,ASTcx,ALTcx,Bilcx,FAcx,INRcx,GGTcx,Kcx,pHcx,Htocx,
                        NAcx,Creatcx,tiempevolcx,tipocx,duracioncx,convcx,timeppostqx,usovasopr,compli,ventprolposqx,uciestposqx,recurrencia,mort,lit,hallazgos,FCqx,FRqx,Sistingqx,Diastqx,
                        Tempqx,tipovasoprd,plaqqx,NSS))

            con.commit()
            con.close()
            st.success('Modificación exitosa')
        
        
                