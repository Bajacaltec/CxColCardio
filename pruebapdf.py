import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

def imprimir_censo(nom):

    left, right = st.columns(2)



    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("template.html")


    left.write("Fill in the data:")
    form = left.form("template_form")
    student = form.text_input("Student name")
    course = form.selectbox(
        "Choose course",
        ["Report Generation in Streamlit", "Advanced Cryptography"],
        index=0,
    )
    grade = form.slider("Grade", 1, 100, 60)
    submit = form.form_submit_button("Generate PDF")

    if submit:

        pdf = pdfkit.from_file(nom, False)
        st.balloons()

        right.success("🎉 Your diploma was generated!")
        # st.write(html, unsafe_allow_html=True)
        # st.write("")
        right.download_button(
            "⬇️ Download PDF",
            data=pdf,
            file_name="diploma.pdf",
            mime="application/octet-stream",
        )