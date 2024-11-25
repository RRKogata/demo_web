import streamlit as st
import pandas as pa

name = st.text_input("Enter Your Name :-")
Fname = st.text_input("Enter your Father Name")
add = st.text_area("Enter Your Address :-")
dob=st.date_input("Enetr Your Date of Birth:-")
classdate= st.selectbox("Enter your Class:-",(1,2))
button= st.button("Submit")

if button:
    st.markdown(f'''
        Name: {name}
        Father's Name: {Fname}
        Address: {add}
        Date of Birth: {dob}
        Class: {classdate}
        ''')