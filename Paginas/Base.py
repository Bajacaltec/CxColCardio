#Código para registrar datos en la base de datos de basecxcolcardio.db

import sqlite3

def conexion_base():
    con = sqlite3.connect('Basecxcol.db')
    cur = con.cursor()
    
def crear_tabla():
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS nombre
              (Nombre TEXT, Edad INT, NSS INT PRIMARY KEY)''')
    
def insertar_datos():
    con = sqlite3.connect('otraprueba.db')
    cur = con.cursor()
    cur.execute("INSERT INTO base VALUES (?,?,?)",(nom,edad,nss))
    con.commit()
    con.close()
    
def seleccionar_datos():
    con = sqlite3.connect('Basecxcol.db')
    cur = con.cursor()
    seleccionar=cur.execute('''Select sum(Edad),sum(NSS) FROM nombre''')
    seleccion=seleccionar.fetchone()

crear_tabla()