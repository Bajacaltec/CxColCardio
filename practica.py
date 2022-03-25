import sqlite3
import streamlit as st
import matplotlib.pyplot as plt

con = sqlite3.connect('Basecxcolcardio.db')
cur = con.cursor()
sumedad=cur.execute('''Select sum(Edad) FROM nombre''')

sum=sumedad.fetchone()
con.commit()
con.close

st.subheader(sum)
st.dataframe(sum)
yu=sum[0]
st.subheader(yu)

con = sqlite3.connect('Basecxcolcardio.db')
cur = con.cursor()
sumnss=cur.execute('''Select NSS FROM nombre''')

sum2=sumnss.fetchall()
con.commit()
con.close
st.subheader(sum2)
st.dataframe(sum2)





