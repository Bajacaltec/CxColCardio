import sqlite3
import streamlit as st
con = sqlite3.connect('Basecxcolcardio.db')
cur = con.cursor()
sumedad=cur.execute('''Select sum(Edad) FROM nombre''')
sum=sumedad.fetchall()
con.commit()

st.subheader(sum)
st.dataframe(sum)
for x in sum:
st.write(x)

