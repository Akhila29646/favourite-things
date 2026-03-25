import streamlit as st
st.title("Registration form")
with st.form("register_form"):
       col1,col2=st.columns(2)
       with col1:
           st.text_input("Enter first name")
       with col2:
           st.text_input("Enter last name")
       age = st.number_input("age",step=1)
       email = st.text_input("Email")
       password=st.text_input("Password",type="password")
       confirm_password=st.text_input("Confirm Password",type="password")
       text=st.text_area("addition info address")
       submitted=st.form_submit_button("Submit")

