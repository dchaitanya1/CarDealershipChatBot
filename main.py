from helper_function import get_db_chain

import streamlit as st

st.title("Car Dealership: Q&A")

question = st.text_input("Question: ")

if question :
    chain = get_db_chain()
    answer = chain.run(question)
    st.header("Answer:")
    st.write(answer)
