import streamlit as st
import pandas as pd

def app():

    df = pd.read_excel("dataset.xlsx")  # read the datset

    st.markdown("## Dataset:")  # add a title
    st.write(df)  # visualize my dataframe in the Streamlit app

    st.markdown("## View your own datset:")
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)