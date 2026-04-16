'''
Create a calculator using Streamlit:
Two number inputs
A selectbox for operations (+, -, *, /)
Display the result when a button is clicked

'''

import streamlit as st

st.title("Simple Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox("Select Operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            st.error("Error: Division by zero!")
            st.stop()
        result = num1 / num2

    st.success(f"Result: {num1} {operation} {num2} = {result}")