from distutils.log import info
import sqlite3
from sqlalchemy import true
import streamlit as st
import resultados
import pandas as pd
from Captura import vitales_ingreso

def slider():
    global diapo
    diapo=st.select_slider('',['Portada','Introducción-1','Introducción-2','Introducción-Diagnóstico de la colecistitis litiásica', 'Introducción-Diagnóstico de la colecistitis alitiásica','Introducción-Tokyo',
                              'Introducción-Complicaciones gastrointestinales en pacientes cardiópatas',
                               'Introducción-Colecistitis aguda en pacientes cardiópatas','Planteamiento del problema',
                               'Justificación','Hipótesis','Objetivos','Objetivos específicos','Objetivos específicos-2','Material y métodos','Criterios de selección','Criterios de exclusión',
                               'Variables','Base de datos','Análisis estadístico','Aspectos éticos','Cronograma','Demográficas','Comorbilidades','Síntomas','Desencadenante de padecimiento actual','Final'])


def introducción():
    if diapo=='Portada':
        st.title('Morbilidad y mortalidad en pacientes con enfermedades cardiovasculares sometidos a colecistectomía por colecistitis aguda en el Centro Médico Nacional Siglo XXI')
        st.caption('Avance de tésis')
        #Como modificar con el st markdown el texto
        #st.markdown(f'<p style="background-color:#7BC9DA;color:#162F34;font-size:32px;border-radius:1%;">La enfermedad vesicular es una de las enfermedades más comunes en el mundo y debe ser quirúrgica o conservadora dependiente del stado en que se encuentra el paciente</p>', unsafe_allow_html=True)
        col1,col2=st.columns(2)

        with col1:
            st.subheader('Dr.Fernando Alonso Núñez Moreno')
            st.caption('UMAE Centro Médico Nacional Siglo XXI, Hospital de especialidades')
            st.subheader('M en C. Vanessa Ortiz Higareda ')
            st.caption('UMAE Centro Médico Nacional Siglo XXI, Hospital de especialidades')
            st.subheader('Dr. Luis León Hernández Trejo')
            st.caption('UMAE Centro Médico Nacional Siglo XXI, Hospital de Cardiología')
            st.caption('29 de junio de 2022')

        with col2:
            st.image('/Users/alonso/CxColCardio/Paginas/Imagenes/CMN SXXI.jpeg')
    elif diapo=='Índice':
        st.title('Índice')
        tol1,tol2,tol3=st.columns(3)
        with tol1:
            st.subheader('I-Introducción')
            st.markdown('Ia-Epidemiología de la colecistitis aguda')
            st.markdown('Ib-Colecistitis litiásica y alitiásica')
            st.markdown('Ic-Clasificación según guías de Tokyo de la colecistitis aguda')
            st.markdown('Id-Diagnóstico de la colecistitis aguda litiásica')
            st.markdown('Ie-Diferencias en el diagnóstico de la colecistitis aguda alitiásica')
            st.markdown('If-Pacientes con enfermedades cardiovasculares y patología quirúrgica gastrointestinal')
            st.markdown('Ig-Pacientes con enfermedades cardiovasculares y colecistitis aguda')
            st.markdown('Ih-Manejo quirúrgico vs tratamiento conservador')


        with tol2:
            st.subheader('II-Justificación')
            st.subheader('III-Planteamiento del problema')
            st.subheader('IV-Objetivos')
            st.markdown('IVa-General')
            st.markdown('IVb-Específicos')
            st.subheader('V-Hipótesis')
            st.subheader('VI-Material y métodos')
            st.markdown('VIa-Tipo de estudio')
            st.markdown('VIb-Población')
        with tol3:
            st.markdown('VIc-Muestra')
            st.markdown('VId-Criterios de selección')
            st.markdown('VIe-Variables')
            st.markdown('VIf-Análisis estadístico')
            st.markdown('VIg-Aspectos éticos')
            st.markdown('IVh-Cronograma')
            

    elif diapo=='Introducción-1':
        sol1,sol2=st.columns(2)
        with sol1:
            Prevalencia = '<p style="font-family:Arial; color:Black; font-size: 35px;">La prevalencia de litiasis vesicular en la población general es de 10-15%</p>'
            st.markdown(Prevalencia, unsafe_allow_html=True)
            st.caption('Pisano M, Allievi N, Gurusamy K, Borzellino G, Cimbanassi S, Boerna D, et al. 2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis. 2020;1–26')

        with sol1:
            new_title = '<p style="background-color:#DAEBF5;color:#12618C;font-size:70px;border-radius:1%;">Epidemiología</p>'
            st.markdown(new_title, unsafe_allow_html=True)

            
        with sol2:
            alitiasica_text = '<p style="font-family:sans-serif; color:#C13719; font-size: 30px;">La incidencia de la colecistitis aguda alitiásica aunque menor respecto a la enfermedad litiásica representa una complicación con alta morbilidad y mortalidad</p>'
            st.markdown(alitiasica_text, unsafe_allow_html=True)
            st.caption('Barie PS. Acute Acalculous Cholecystitis. Gastroenterol Clin NA [Internet]. 2010;39(2):343–57')
            st.image('epidemio.png',width=350)
   
        vol1,vol2=st.columns(2)
        with sol1:
            new_title = '<p style="font-family:sans-serif; color:Black; font-size: 35px;">20-40% de los pacientes desarrollarán complicaciones relacionadas con litiasis vesicular</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.caption('Pisano M, Allievi N, Gurusamy K, Borzellino G, Cimbanassi S, Boerna D, et al. 2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis. 2020;1–26')
        
        
   
    elif diapo=='Introducción-2':
        col1,col2=st.columns(2)
        with col1:
            st.subheader('Colecistitis aguda litiásica')
            litiasis_vesicular_text = '<p style= "background-color:#DAEBF5;font-family:Arial; color:#12618C; font-size: 25px;">Proceso inflamatorio de la vesícula biliar ocasionado por litos vesículares que obstruyen el cuello vesícular o el cístico</p>'
            st.markdown(litiasis_vesicular_text, unsafe_allow_html=True)
            st.caption('Adachi T, Eguchi S, Muto Y. Pathophysiology and pathology of acute cholecystitis: A secondary publication of the Japanese version from 1992. J Hepatobiliary Pancreat Sci. 2021;1–5.')

            st.image('/Users/alonso/CxColCardio/ccli.gif')

        with col2:
            st.subheader('Colecistitis alitiásica')
            alitiasis_vesicular_text = '<p style= "background-color:#DAEBF5;font-family:Arial; color:#12618C; font-size: 20px;">La colecistitis alitiásica se debe a un estado necroinflamatorio de la vesícula biliar en el cual no existe una obstrucción del conducto cístico</p>'

            st.markdown(alitiasis_vesicular_text,unsafe_allow_html=True)
            st.caption('Barie PS. Acute Acalculous Cholecystitis. Gastroenterol Clin NA [Internet]. 2010;39(2):343–57.')
            st.image('alit5.png')
            st.info('La obstrucción del conducto cístico en casos donde no ocurre colecistitis aguda, sugiere que la oclusión de esta estructura no es suficiente para desarrollar la enfermedad y se requiere la obstrucción de la arteria cística al menos parcialmente')
            st.caption('Adachi T, Eguchi S, Muto Y. Pathophysiology and pathology of acute cholecystitis: A secondary publication of the Japanese version from 1992. J Hepatobiliary Pancreat Sci. 2021;1–5')
    
    elif diapo=='Introducción-Tokyo':
        st.title('Clasificación de la colecistitis aguda')
        df_tokyo=pd.read_excel('/Users/alonso/CxColCardio/tokyo_tabla.xlsx')
        df_tokyo.dropna(axis = 0, how ='any', thresh = None, subset = None, inplace=False)
        st.table(df_tokyo)
        st.caption('Modificado de Yokoe M, Hata J, Takada T, Strasberg SM, Asbun HJ, Wakabayashi G, et al. Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos). J Hepatobiliary Pancreat Sci. 2018;25(1):41–54')
    
    elif diapo=='Introducción-Diagnóstico de la colecistitis litiásica': 
        st.title('Diagnóstico de la colecistitis aguda litiásica')   
        st.subheader('El diagnóstico de la colecistitis aguda litiásica se realiza al identificar signos locales de inflamación, signos sistémicos y datos sugestivos obtenidos por imagen')
        dxcole=pd.read_excel('/Users/alonso/CxColCardio/dx cole.xlsx')
        dxcole.dropna
        st.table(dxcole)
        st.caption('Modificado de Yokoe M, Hata J, Takada T, Strasberg SM, Asbun HJ, Wakabayashi G, et al. Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos). J Hepatobiliary Pancreat Sci. 2018;25(1):41–54')
    
    elif diapo=='Introducción-Diagnóstico de la colecistitis alitiásica': 
        st.title('Diagnóstico de la colecistitis aguda alitiásica')   
        col1,col2=st.columns(2)
        with col1:
            st.subheader('El diagnóstico en la colecistitis alitiásica es difícil, los pacientes suelen estar críticamente enfermos y son incapaces de comunicar sus síntomas')
            st.caption('Barie PS. Acute Acalculous Cholecystitis. Gastroenterol Clin NA [Internet]. 2010;39(2):343–57.')

        with col2:
            st.subheader('La exploración física y los laboratorios no son confiables y el diagnóstico suele estar basado en estudios radiológicos ')
        st.info('El ultrasonido de la vesícula biliar es el método diagnóstico más acertada para el diagnóstico de la colecistitis aguda en el paciente crítico.')
        st.subheader('El grosor de la pared vesícular mayor a 3.5 mm se acepta como diagnóstico para colecistitis alitiásica, otros signos importantes incluyen líquido pericolecístico o la presencia de gas intramural o una capa sonolúcida que representa edema intramural')
        st.caption('Yokoe M, Hata J, Takada T, Strasberg SM, Asbun HJ, Wakabayashi G, et al. Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos). J Hepatobiliary Pancreat Sci. 2018;25(1):41–54')
    
    
    elif diapo=='Introducción-Complicaciones gastrointestinales en pacientes cardiópatas': 
        st.title('Complicaciones gastrointestinales en pacientes cardiópatas')
        st.subheader('Las complicaciones gastrointestinales en pacientes cardiópatas se deben a la hipoperfusión esplácnica, esta actúa como un reservorio conteniendo aproximadamente 800 ml de sangre que puede ser desplazada a la circulación general en caso de hipovolemia, este desplazamiento de sangre puede llevar a complicaciones en los órganos gastrointestinales')
        st.caption('Chor CYT, Mahmood S, Khan IH, Shirke M, Harky A. Gastrointestinal complications following cardiac surgery. Asian Cardiovasc Thorac Ann. 2020;28(9):621–32. ')
        fol1,fol2=st.columns(2)

        with fol1:
            st.info('Las complicaciones gastrointestinales que se presentan en pacientes cardiópatas especialmente después de cirugía de corazón están históricamente asociadas con una alta morbilidad y mortalidad, en algunas series la mortalidad alcanza  hasta 70% ')
            st.caption('Pisano M, Allievi N, Gurusamy K, Borzellino G, Cimbanassi S, Boerna D, et al. 2020 World Society of Emergency Surgery updated guidelines for the diagnosis and treatment of acute calculus cholecystitis. 2020;1–26')
            st.success('Gulkarov realizó una investigación en pacientes sometidos a cirugía por patología de válvula mitral de 565 pacientes 13 presentarón complicaciones gastrointestinales con una incidencia de 2.3%, presentando una mortalidad de 38%')
            st.caption('Gulkarov I, Trocciola SM, Yokoyama CC, Girardi LN, Krieger KK, Wayne Isom O, et al. Gastrointestinal complications after mitral valve surgery. Ann Thorac Cardiovasc Surg. 2014;20(4):292–8')
        with fol2:
            st.error('La incidencia se estima en múltiples publicaciones en 0.3-5.5%, las complicaciones gastrointestinales más frecuentes fue la infección por C.difficile (33.6%), sangrado de tubo digestivo (30.7%), Falla hepática (23.6%), Ileo prolongado (21.1%), isquemia mesentérica (16.8%), colecistitis aguda (6%) y pancreatitis en 5%., los pacientes con complicaciones gastrointestinales tuvieron un mayor riesgo de muerte ')
            st.caption('Haywood N, Mehaffey JH, Hawkins RB, Zhang A, Kron IL, Kern JA, et al. ScienceDirect Association for Academic Surgery Gastrointestinal Complications After Cardiac Surgery : Highly Morbid but Improving Over Time. J Surg Res [Internet]. 2020;254(434):306–13')
            
    elif diapo=='Introducción-Colecistitis aguda en pacientes cardiópatas': 
        st.title('Colecistitis aguda en pacientes cardiópatas')
        st.subheader('En un estudio de casos de mas de 16,000  pacientes sometidos a cirugía cardiovascular se encontró  una incidencia de colecistitis aguda litiásica de 0.03%  y de 0.08% para colecistitis alitiásica en pacientes sometidos a cirugía cardiaca')
        gol1,gol2=st.columns(2)
        with gol1:
            st.info('En el grupo que desarrolló colecistitis alitiásica se incluyeron 13 pacientes, siete fueron tratados de manera conservadora y seis con cirugía, con tres muertes (23%) y todas ocurrieron en los pacientes tratados de manera quirúrgica')
            st.caption('Passage J, Joshi P, Mullany D V. Acute Cholecystitis Complicating Cardiac Surgery : Case Series Involving More Than 16 , 000 Patients. 2007; ')
            st.warning('Estudio retrospectivo con 90 pacientes sometidos a colecistostomia y 556 a colecistectomía. De los 90 pacientes sometidos a colecistostomía percutanea 13 requirieron colecistectomía')
            st.caption('Greca ALA, Grezia MDI, Magalini S, Giorgio ADI, Lodoli C, Flumeri GDI, et al. Comparison of cholecystectomy and percutaneous cholecystostomy in acute cholecystitis : results of a retrospective study. 2017;4668–74')
        with gol2:
            st.success('En el grupo con colecistitis litiásica se incluyeron 5 pacientes que desarrollaron colecistitis aguda, 3 fueron sometidos a cirugía y 2 fueron manejados de manera conservadora, hubo una defunción en el grupo de la colecistectomía al 6to día')
            st.caption('Passage J, Joshi P, Mullany D V. Acute Cholecystitis Complicating Cardiac Surgery : Case Series Involving More Than 16 , 000 Patients. 2007; ')
            st.warning('Estudio con dos grupos uno con manejo quirúrgico y otro manejo no quirúrgico en pacientes con colecistitis alitiásica, 48 pacientes fueron sometidos a colecistectomía y 41 de manera no quirúrgica, las complicaciones fueron mayores en el grupo quirúrgico vs no quirúrgico 18.8% vs 2.4% respectivamente')
            st.caption('Kim SB, Gu MG, Kim KH, Kim TN. Long-term outcomes of acute acalculous cholecystitis treated by non-surgical management. Med (United States). 2020;99(7):1–4. ')
    elif diapo=='Introducción-Manejo quirúrgico vs conservador': 
        st.title('Manejo quirúrgico vs conservador')
        st.info('En el estudio de Kim et al., 2014 se comparó el desenlace clínico en dos grupos uno con manejo quirúrgico y otro manejo no quirúrgico en pacientes con colecistitis alitiásica, se incluyeron 89 pacientes 48 fueron sometidos a colecistectomía de manera inicial, 41 pacientes fueron tratados de manera no quirúrgica, con 27 pacientes tratados con antibióticos exclusivamente y 14 pacientes fueron manejados con colecistostomía percutánea. No hubo diferencia entre la estancia intrahospitalaria entre los grupos analizados, la prevalencia de complicaciones fue significativamente mayor en el grupo quirúrgico con 18.8% y 2.4% en el grupo no quirúrgico, durante el seguimiento a 5.7 años hubo recurrencia en 9.8% de los pacientes del grupo no quirúrgico ')
        st.caption('Kim SB, Gu MG, Kim KH, Kim TN. Long-term outcomes of acute acalculous cholecystitis treated by non-surgical management. Med (United States). 2020;99(7):1–4.')
        st.info('En un retrospectivo se incluyeron 646 pacientes con colecistitis aguda, 90 pacientes fueron sometidos a colecistostomía percutánea y 556 se realizaron colecistectomía, de los 90 pacientes sometidos a colecistostomia percutánea 13 requirieron colecistectomía electiva. En general, las complicaciones postoperatorias y la mortalidad hospitalaria fueron mayores en pacientes que fueron tratados con colecistostomía percutánea vs colecistectomía. De los 90 pacientes que fueron sometidos a colecistostomia percutánea 13, requirieron colecistectomía en la misma hospitalización, 77 fueron dados de alta con el drenaje, de estos 12 desarrollaron complicaciones  biliares como colecistitis (4), salida del drenaje (5), coledocolitiasis (3), y 5 requirieron  una sustitución del drenaje(17). ')
        st.success('En otro estudio qué incluyó 271 pacientes con colecistitis alitiásica tratada con colecistostomía percutánea, se consiguió la resolución sintomática y normalización de los parámetros de laboratorio en 86.7% (235 pacientes) cuatro días después de la colecistostomía percutánea. Se observaron complicaciones en seis pacientes.  La colecistectomía de intervalo fue realizada en 46.8% de los pacientes y de los 121 pacientes restantes se retiro exitosamente el catéter de colecistostomia en un tiempo promedio de 30 días.  Del grupo a quien se le retiro el catéter este fue exitoso en 97.7% mientras que dos (2.3%) sufrieron una recurrencia de la colecistitis, la recurrencia acumulada fue de 1.1%, 2.7% y 2.7% en 1,2, y ocho años respectivamente(18).')
    
    elif diapo=='Planteamiento del problema':
        st.title('Planteamiento del problema')
        st.subheader('Los pacientes con enfermedades cardiovasculares pueden presentar complicaciones gastrointestinales, como es la colecistitis aguda; a pesar de que existe evidencia para el manejo de este tipo de pacientes, la morbilidad y mortalidad siguen siendo elevadas.')
   
    elif diapo=='Justificación':
        st.title('Justificación')
        st.subheader('El conocer los factores de riesgo, la evolución clínica y la morbimortalidad de los pacientes con colecistitis aguda y  enfermedades cardiovasculares permitirá proponer nuevas medidas terapéuticas capaces de influir positivamente en la evolución clínica de esta población de alto riesgo')

    elif diapo=='Objetivos':
        st.title('Objetivo general')
        st.subheader('Conocer las características clínicas y epidemiológicas de los pacientes con enfermedades cardiovasculares o cirugía cardiopulmonar reciente del Centro Médico Nacional Siglo XXI, que desarrollaron colecistitis aguda, y  determinar la morbilidad y mortalidad de la colecistectomía (urgente o programada)  en este mismo grupo. Determinar si existen factores de riesgo para complicaciones posoperatorias entre ellos')
    elif diapo=='Objetivos específicos':
        st.title('Objetivo específicos')
        st.subheader('•	Conocer las caracteristicas clínicas y epidemiológicas de los pacientes sometidos a colecistectomía con enfermedades cardiovasculares  del Centro Médico Nacional siglo XXI.')
        st.subheader('•	Determinar factores predictivos clínicos que aumentan la morbilidad y mortalidad de pacientes con enfermedades cardiovasculares que se complican con colecistitis aguda')
        st.subheader('•	Valorar el uso de marcadores bioquímicos como predictores de un aumento en la morbilidad y morbilidad de pacientes con enfermedades cardiovasculares que se complican con colecistitis aguda')
        st.subheader('•	Evaluar la efectividad de scores clínicos (APACHE II, SOFA, ASA) que predigan el aumento de morbilidad y morbilidad de pacientes con enfermedades cardiovasculares que se complican con colecistitis aguda')
        
    elif diapo=='Objetivos específicos-2':
        st.title('Objetivos específicos')
        st.subheader('•	Identificar si existe un aumento en la morbilidad y mortalidad de pacientes sometidos a colecistectomía por colecistitis aguda alitiásica vs colecistitis aguda litiásica')
        st.subheader('•	Observar cuales son las complicaciones postoperatorias más comunes en pacientes sometidos a colecistectomía por colecistitis aguda')
        st.subheader('•	Comparar el impacto en la morbilidad y mortalidad del inicio del cuadro de colecistitis aguda y el momento en que se realiza la colecistectomía')
        st.subheader('•	Analizar si el manejo no quirúrgico (colecistostomía, antibióticos) conlleva una menor morbimortalidad comparada con el tratamiento quirúrgico')


    elif diapo=='Hipótesis':
        st.title('Hipótesis')
        st.subheader('Existen factores predictores en pacientes con enfermedades cardiovasculares con un cuadro de colecistitis aguda que nos permiten determinar que pacientes están en riesgo de una mayor  morbilidad y mortalidad, así como una diferencia significativa en la morbilidad y mortalidad en pacientes con colecistitis alitiásica vs colecistitis litiásica')
        
    elif diapo=='Material y métodos':
        st.title('Material y métodos')
        st.subheader('Tipo de estudio')
        st.subheader('Observacional, analítico, retrospectivo, transversal')
        
        st.subheader('Población')
        st.subheader('Pacientes operados en el Hospital de Cardiología o en el Hospital de Especialidades del Centro Médico Nacional Siglo XXI que ingresaron por patología cardiaca o son sometidos a cirugía cardiopulmonar y durante su mismo internamiento presentan como complicación colecistitis aguda, valorados por el servicio de Gastrocirugia del Hospital de Especialidades en el periodo comprendido entre enero 2017 y  enero 2022')
        
        #st.subheader('Muestra')
        #st.subheader('Se incluirán a todos los pacientes con enfermedad cardiovascular como motivo de ingreso y que presentan como complicación colecistitis aguda, (alitiásica o litiásica) que fueron sometidos a colecistectomía o fueron manejados de manera conservadora durante el periodo de estudio')
    
    elif diapo=='Criterios de selección':
        st.title('Criterios de inclusión')
        st.subheader('•	Pacientes con enfermedad cardiovascular como motivo de ingreso y/o PO de cirugía cardiopulmonar y qué durante el mismo internamiento presentan como complicación colecistitis aguda, (alitiásica o litiásica) ')
        st.subheader('•	Pacientes que cuenten con expediente clínicos en el hospital de cardiología y/o hospital de especialidades de Centro Médico Nacional siglo XXI')
        st.subheader('•	Valorados por el servicio de Gastrocirugía del Hospital de Especialidades')
        st.subheader('•	Pacientes que cuenten con diagnóstico clínico con base en guías de Tokyo, hallazgos transquirúrgicos o histopatológicos compatibles con colecistitis aguda')
        st.subheader('•	Pacientes mayores de 18 años')
        
    elif diapo=='Criterios de exclusión':
        st.title('Criterios de exclusión')
        st.subheader('• Pacientes que no cuenten con antecedentes de enfermedad cardiovascular o que no se sometieran a procedimientos cardiovasculares previo al inicio del padecimiento actual')
        st.subheader('•	Pacientes que durante el procedimiento quirúrgico presenten patología abdominal diferente a la colecistitis aguda como trombosis mesentérica, pancreatitis aguda, etc')
        st.subheader('•	Pacientes que no cumplan con los criterios clínicos, hallazgos transquirúrgicos o reporte de histopatología compatible con colecistitis aguda')
    elif diapo=='Variables':
        st.title('Variables')
        variables=pd.read_excel('/Users/alonso/CxColCardio/variables.xlsx')
        st.table(variables)
        
    elif diapo=='Base de datos':
        st.title('Hoja de recolección de datos')
        con=sqlite3.connect('DB.db')
        cur=con.cursor()
        base_df=cur.fetchall()
        df_base=pd.read_excel('/Users/alonso/CxColCardio/recol_datos.xlsx')
        st.table(df_base)
    
    elif diapo=='Análisis estadístico':
        st.title('Análisis estadístico')
        st.subheader('El análisis estadístico descriptivo se llevará a cabo utilizando bibliotecas de Python como Matplotlib, Pandas y Numpy utilizando medianas, medias, rangos y medidas de tendencia central, se incluirán medidas paramétricas y no paramétricas (T de student, Chi 2, Mann Whitney). ')
    
    elif diapo=='Aspectos éticos':
        st.title('Aspectos éticos')
        st.subheader('''Se tomarán en cuenta aspectos de seguridad y confidencialidad garantizando el anonimato de los pacientes incluidos en la base de datos, en estricto apego a la norma para la investigación científica y/o desarrollo tecnológico en salud en el Instituto Mexicano del Seguro Social (Norma 2000-001-009) con última actualización del 5 de noviembre de 2021''')
        st.caption('Se declara que los procedimientos de el presente trabajo para la titulación se apegan a las normas éticas y a los reglamentos institucionales del Instituto Mexicano del Seguro Social de acuerdo al Departamento de Investigación Científica, al reglamento de la ley general de salud en materia de investigación así como a las normas internacionales como la declaración de Helsinki y de acuerdo al Reglamento de la Ley General de Salud, en Materia de Investigación para la salud')
        st.subheader('Autorización por parte del comité local de investigación con número de registro institucional')
        st.info('R-2022-3601-140')
    
    
    elif diapo=='Cronograma':
        st.title('Cronograma')
        df_excel = pd.read_excel('/Users/alonso/CxColCardio/df.xlsx')
        df_excel.fillna(method ='pad')
        
        st.table(df_excel)

def comorbilidades_res():
    if diapo=='Comorbilidades':
        st.title('Comorbilidades')
        resultados.comorb()
            
def resultados_biométricos():
    if diapo=='Demográficas':
        st.title('Características demográficas')

        col1,col2=st.columns(2)
        with col1:
            st.subheader('Edad')
            resultados.edad()
            st.info('Media 62')
            st.info('El rango va de 24 a 92 años')
            st.info('La mediana es de 63')
        with col2:
            st.subheader('Género')
            resultados.contar_genero()
        
def sintomas_ccla():
    if diapo=='Síntomas':
        resultados.sintomas_ccla()

def desencadenantes_enfermedad():
    if diapo=='Desencadenante de padecimiento actual':
        st.title('Patología desencadenante de padecimiento actual')
        resultados.comor_PA()
        st.info('El desencadenante más común del padecimiento actual en pacientes con colecistitis aguda es el infarto agudo al miocardio, seguido por cirugía cardiovascular reciente')
        
def mortalidad():
    if diapo=='Mortalidad':
        st.title('Mortalidad')
        resultados.mortalidad()
        
    elif diapo=='Final':
        st.title('¿Comentarios?')
        st.balloons()
            
