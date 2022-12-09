import streamlit as st
from streamlit_lottie import st_lottie
from utils import *

import pandas as pd

st.set_page_config(
        page_icon="🤳",
        page_title = "Fantastic QR Code Gen",
        layout="centered"
    )

st.header("Batch Barcoder Generator")
hide_footer()

st.markdown("--------Work in Progress------")
try:
    uploaded_file = st.file_uploader(label="Upload a csv file",type=["csv"])
    if uploaded_file is not None:
        st.snow()
        # Read the Dataframe
        data_df = pd.read_csv(uploaded_file)
        # Display the Dataframe
        st.markdown("### Input Dataframe")
        st.dataframe(data_df,height=200)
        st.button("Generate QR Codes")
except:
    st.error("Please upload an appropriate CSV file")
